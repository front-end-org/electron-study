{
    "targets":[
        {
            "target_name":"fingerprint",
            "cflags!":["-fno-exceptions"],
            "sources":['fingerprint.cc'],
            "include_dirs":[
                "<!@(node -p \"require('node-addon-api).include\")"
            ],
            "defines":['NAPI_DISABLE_CPP_EXCEPTIONS'],
        }
    ]
}