POST /bookdb_index/book/_search
{
    "query": {
        "multi_match" : {
            "query" : "elasticsearch guide",
            "fields": ["title", "summary"]
        }
    }
}
#Thêm xem sao


#okie