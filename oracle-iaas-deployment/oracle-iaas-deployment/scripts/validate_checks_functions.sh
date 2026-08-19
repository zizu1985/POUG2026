check_business_service() {
    if [ -z "$business_service" ]; then  
        echo "business_service input failure -> adding to failed fields"
        failed_fields+=("business_service")
    elif [ "$GITLAB_USER_LOGIN" != "snow_token" ]; then
        snow cmdb resolve_ci_name --env="$SNOW_ENVIRONMENT" -c "$business_service" --mulesoft_id "$MULESOFT_ID" --mulesoft_secret "$MULESOFT_SECRET" --username "$SNOW_USERNAME" --password "$SNOW_PASSWORD" --sourcesystemid "$SNOW_SOURCESYSTEMID" | tee check_service.json
        SRV_REC_CNT=$(cat check_service.json | jq ".result.recAllCount")
        if [[ $SRV_REC_CNT -ge 1 ]]; then
            echo "business service exists in ServiceNow"
        else
            echo "business_service does not exist in ServiceNow"
            echo "business_service input failure - adding to failed fields"
            failed_fields+=("business_service")
        fi
    fi
}
check_server() {
    if [ -z "$server" ]; then
        echo "server input failure -> adding to failed fields"
        failed_fields+=("server")
    elif [ "$GITLAB_USER_LOGIN" != "snow_token" ]; then
        snow cmdb get_ci_details -c $server --env=$SNOW_ENVIRONMENT --mulesoft_id ${MULESOFT_ID} --mulesoft_secret ${MULESOFT_SECRET} --username ${SNOW_USERNAME} --password ${SNOW_PASSWORD} --sourcesystemid ${SNOW_SOURCESYSTEMID} | tee check_ci.json
        SRV_CNT=$(cat check_ci.json | jq ".result")
        if [ ${#SRV_CNT} > 4 ]; then
            export SRV_CNT=${SRV_CNT:0:4}
        fi
        if [ $SRV_CNT = '[]' ]; then
            echo "server does not exist in ServiceNow."
            echo "server input failure -> adding to failed fields"
            failed_fields+=("server")
        fi     
    fi
}
check_db_name() {
    if [ -z "$db_name" ]; then
        echo "db_name input failure -> adding to failed fields"
        failed_fields+=("db_name")
    elif [ ${#db_name} -ge 9 ]; then
        echo "db_name input failure -> db_name has more than 8 characters"
        echo "db_name input failure -> adding to failed fields"
        failed_fields+=("db_name")
    fi
}
check_size_db() {
    if [ -z "$size_db" ]; then
        echo "size_db input failure -> adding to failed fields"
        failed_fields+=("size_db")
    else
        re='^[0-9]+$'
        if ! [[ $size_db =~ $re ]] ; then
            echo "size_db input failure -> it is not a integer"
            echo "size_db input failure -> adding to failed fields"
            failed_fields+=("size_db")
        fi
    fi
}
check_level_support() {
    if [ -z "$level_support" ]; then
        echo "level_support input failure -> adding to failed fields"
        failed_fields+=("level_support")
    elif [ $GITLAB_USER_LOGIN != "snow_token" ]; then
        found=0
        for x in 'Production' 'Test' 'Development' 'Sandpit'; do
            if [ $x = $level_support ]; then
                found=1
            fi    
        done
        if [ $found = 0 ]; then
            echo "level_support not in allowed values"
            echo "level_support input failure -> adding to failed fields"
            failed_fields+=("level_support")
        fi
    fi
}
check_version() {
    if [ -z "$version" ]; then
        echo "version input failure -> adding to failed fields"
        failed_fields+=("version")
    elif [ $GITLAB_USER_LOGIN != "snow_token" ]; then
        found=0
        for x in '12.2' '18.3' '18.6' '18.8' '18.12' '18.13' '18.14' '19.14'  '19.15' '19.17' '19.18' '19.19' '19.20' '19.21' '19.22' '19.23' '19.24' '19.26' '19.27' '19.28' '19.29'; do
            if [ $x = $version ] ; then
                found=1
            fi
        done
        if [ $found = 0 ]; then
            echo "version not in allowed values"
            echo "version input failure -> adding to failed fields"
            failed_fields+=("version")
        fi 
    fi
}
check_os_majorversion() {
	if [ -z "$os_majorversion" ]; then
        echo "os_majorversion input failure -> adding to failed fields"
        failed_fields+=("os_majorversion")
    else
        found=0
        for x in '7' '8' '9'; do
            if [ $x = $os_majorversion ] ; then
                found=1
            fi
        done
        if [ $found = 0 ]; then
            echo "os_majorversion not in allowed values"
            echo "os_majorversion input failure -> adding to failed fields"
            failed_fields+=("os_majorversion")
        fi 
    fi
}
check_version_for_rhel9() {
    found=0
    for x in '19.22' '19.23' '19.24' '19.26' '19.27' '19.28' '19.29'; do
        if [ $x = $version ] ; then
            found=1
        fi
    done
    if [ $found = 0 ]; then
        echo "version not supported in rhel9"
        echo "version support on rhel9 failure -> adding to failed fields"
        failed_fields+=("version_not_supported_on_rhel9")
    fi 
}
