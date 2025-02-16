self.__uv$config = {
    prefix: '/app/login/',
    bare: "https://sysadmin.us.kg/",
    encodeUrl: Ultraviolet.codec.xor.encode,
    decodeUrl: Ultraviolet.codec.xor.decode,
    handler: '/app/uv/uv.handler.js',
    bundle: '/app/uv/uv.bundle.js',
    config: '/app/uv/uv.config.js',
    sw: '/app/uv/uv.sw.js',
};
