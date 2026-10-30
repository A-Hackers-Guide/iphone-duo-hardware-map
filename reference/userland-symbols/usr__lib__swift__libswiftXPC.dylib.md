# Symbols: `/usr/lib/swift/libswiftXPC.dylib`

Symbol table of this image in the iOS 27.2 dyld shared cache (`ipsw dyld macho -n --demangle`). The class-level view is on the [image page](../userland/usr__lib__swift__libswiftXPC.dylib.md). **[DSC]**

608 public symbols, 1,486 private symbols, 0 undefined (imported).

## Public (external)

```
0x1946dfd30  __TEXT,__text  XPC.xpc_uuid_get_uuid(__C.OS_xpc_object) -> (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)?
0x1946df23c  __TEXT,__text  XPC.xpc_session_create_xpc_service(Swift.UnsafePointer<Swift.Int8>, __C.OS_dispatch_queue?, XPC.xpc_session_create_flags_t, Swift.AutoreleasingUnsafeMutablePointer<__C.OS_xpc_object?>?) -> __C.OS_xpc_object?
0x1946dfd6c  __TEXT,__text  XPC.xpc_uuid_create_with_uuid((Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)) -> __C.OS_xpc_object
0x1946df12c  __TEXT,__text  XPC.XPC_BOOL_TRUE.getter : __C.OS_xpc_object
0x1946def14  __TEXT,__text  XPC.XPC_TYPE_BOOL.getter : Swift.OpaquePointer
0x1946deef4  __TEXT,__text  XPC.XPC_TYPE_DATA.getter : Swift.OpaquePointer
0x1946def50  __TEXT,__text  XPC.XPC_TYPE_DATE.getter : Swift.OpaquePointer
0x1946def44  __TEXT,__text  XPC.XPC_TYPE_NULL.getter : Swift.OpaquePointer
0x1946df09c  __TEXT,__text  XPC.XPC_TYPE_PIPE.getter : Swift.OpaquePointer
0x1946def68  __TEXT,__text  XPC.XPC_TYPE_UUID.getter : Swift.OpaquePointer
0x1946df158  __TEXT,__text  XPC.XPC_BOOL_FALSE.getter : __C.OS_xpc_object
0x1946def08  __TEXT,__text  XPC.XPC_TYPE_ARRAY.getter : Swift.OpaquePointer
0x1946c2b8c  __TEXT,__text  XPC.XPC_TYPE_ERROR.getter : Swift.OpaquePointer
0x1946def20  __TEXT,__text  XPC.XPC_TYPE_INT64.getter : Swift.OpaquePointer
0x1946def80  __TEXT,__text  XPC.XPC_TYPE_SHMEM.getter : Swift.OpaquePointer
0x1946df0a8  __TEXT,__text  XPC.XPC_TYPE_BUNDLE.getter : Swift.OpaquePointer
0x1946def38  __TEXT,__text  XPC.XPC_TYPE_DOUBLE.getter : Swift.OpaquePointer
0x1946def5c  __TEXT,__text  XPC.XPC_TYPE_STRING.getter : Swift.OpaquePointer
0x1946def2c  __TEXT,__text  XPC.XPC_TYPE_UINT64.getter : Swift.OpaquePointer
0x1946def00  __TEXT,__text  XPC.XPC_ARRAY_APPEND.getter : Swift.Int
0x1946df084  __TEXT,__text  XPC.XPC_TYPE_POINTER.getter : Swift.OpaquePointer
0x1946df0b4  __TEXT,__text  XPC.XPC_TYPE_SERVICE.getter : Swift.OpaquePointer
0x1946df078  __TEXT,__text  XPC.XPC_TYPE_ACTIVITY.getter : Swift.OpaquePointer
0x1946def98  __TEXT,__text  XPC.XPC_TYPE_ENDPOINT.getter : Swift.OpaquePointer
0x1946a8198  __TEXT,__text  XPC.XPC_EVENT_KEY_NAME.getter : Swift.UnsafePointer<Swift.Int8>
0x1946defa4  __TEXT,__text  XPC.XPC_TYPE_MACH_RECV.getter : Swift.OpaquePointer
0x1946def8c  __TEXT,__text  XPC.XPC_TYPE_MACH_SEND.getter : Swift.OpaquePointer
0x1946beae0  __TEXT,__text  XPC.XPC_TYPE_CONNECTION.getter : Swift.OpaquePointer
0x1946beab8  __TEXT,__text  XPC.XPC_TYPE_DICTIONARY.getter : Swift.OpaquePointer
0x1946defbc  __TEXT,__text  XPC.XPC_TYPE_RICH_ERROR.getter : Swift.OpaquePointer
0x1946df090  __TEXT,__text  XPC.XPC_TYPE_SERIALIZER.getter : Swift.OpaquePointer
0x1946df0cc  __TEXT,__text  XPC.XPC_TYPE_FILE_TRANSFER.getter : Swift.OpaquePointer
0x1946defb0  __TEXT,__text  XPC.XPC_TYPE_MACH_SEND_ONCE.getter : Swift.OpaquePointer
0x1946df0f0  __TEXT,__text  XPC.XPC_ERROR_KEY_DESCRIPTION.getter : Swift.UnsafePointer<Swift.Int8>
0x1946df0c0  __TEXT,__text  XPC.XPC_TYPE_SERVICE_INSTANCE.getter : Swift.OpaquePointer
0x1946c2b9c  __TEXT,__text  XPC.XPC_ERROR_CONNECTION_INVALID.getter : __C.OS_xpc_object
0x1946df1b0  __TEXT,__text  XPC.XPC_ERROR_TERMINATION_IMMINENT.getter : __C.OS_xpc_object
0x1946df184  __TEXT,__text  XPC.XPC_ERROR_CONNECTION_INTERRUPTED.getter : __C.OS_xpc_object
0x1946df1dc  __TEXT,__text  XPC.XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT.getter : __C.OS_xpc_object
0x1946def74  __TEXT,__text  XPC.XPC_TYPE_FD.getter : Swift.OpaquePointer
0x1946ddc94  __TEXT,__text  XPC.XPCSession.auditToken.getter : __C.audit_token_t
0x1946e2fa4  __TEXT,__const  property descriptor for XPC.XPCSession.auditToken : __C.audit_token_t
0x1946ded38  __TEXT,__text  dispatch thunk of XPC.XPCSession.rejectPeer(reason: Swift.String) -> ()
0x1946e3c3c  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.rejectPeer(reason: Swift.String) -> ()
0x1946dcc98  __TEXT,__text  XPC.XPCSession.__allocating_init(xpcService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, requirement: XPC.XPCPeerRequirement, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946dccc4  __TEXT,__text  XPC.XPCSession.__allocating_init(xpcService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, requirement: XPC.XPCPeerRequirement, incomingMessageHandler: ((XPC.XPCDictionary) -> XPC.XPCDictionary?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) 
0x1946dcd3c  __TEXT,__text  XPC.XPCSession.__allocating_init(xpcService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, requirement: XPC.XPCPeerRequirement, incomingMessageHandler: ((XPC.XPCReceivedMessage) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ())
0x1946dccfc  __TEXT,__text  XPC.XPCSession.__allocating_init<A where A: Swift.Decodable>(xpcService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, requirement: XPC.XPCPeerRequirement, incomingMessageHandler: ((A) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError)
0x1946da574  __TEXT,__text  XPC.XPCSession.__allocating_init(xpcService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946da58c  __TEXT,__text  XPC.XPCSession.__allocating_init(xpcService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((XPC.XPCDictionary) -> XPC.XPCDictionary?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946da60c  __TEXT,__text  XPC.XPCSession.__allocating_init(xpcService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((XPC.XPCReceivedMessage) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946da5a4  __TEXT,__text  XPC.XPCSession.__allocating_init<A where A: Swift.Decodable>(xpcService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((A) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946dd190  __TEXT,__text  XPC.XPCSession.__allocating_init(machService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, requirement: XPC.XPCPeerRequirement, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946dd320  __TEXT,__text  XPC.XPCSession.__allocating_init(machService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, requirement: XPC.XPCPeerRequirement, incomingMessageHandler: ((XPC.XPCDictionary) -> XPC.XPCDictionary?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?)
0x1946dd6f8  __TEXT,__text  XPC.XPCSession.__allocating_init(machService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, requirement: XPC.XPCPeerRequirement, incomingMessageHandler: ((XPC.XPCReceivedMessage) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ()
0x1946dd500  __TEXT,__text  XPC.XPCSession.__allocating_init<A where A: Swift.Decodable>(machService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, requirement: XPC.XPCPeerRequirement, incomingMessageHandler: ((A) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError
0x1946a8274  __TEXT,__text  XPC.XPCSession.__allocating_init(machService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946daa68  __TEXT,__text  XPC.XPCSession.__allocating_init(machService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((XPC.XPCDictionary) -> XPC.XPCDictionary?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946dac48  __TEXT,__text  XPC.XPCSession.__allocating_init(machService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((XPC.XPCReceivedMessage) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946daa80  __TEXT,__text  XPC.XPCSession.__allocating_init<A where A: Swift.Decodable>(machService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((A) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946dc17c  __TEXT,__text  XPC.XPCSession.__allocating_init(fromConnection: __C.OS_xpc_object, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946dc574  __TEXT,__text  XPC.XPCSession.__allocating_init(fromConnection: __C.OS_xpc_object, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((XPC.XPCDictionary) -> XPC.XPCDictionary?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946a520c  __TEXT,__text  XPC.XPCSession.__allocating_init(fromConnection: __C.OS_xpc_object, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((XPC.XPCReceivedMessage) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946dcb10  __TEXT,__text  XPC.XPCSession.__allocating_init<A where A: Swift.Decodable>(fromConnection: __C.OS_xpc_object, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((A) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCS
0x1946c12b4  __TEXT,__text  dispatch thunk of XPC.XPCSession.setTargetQueue(__C.OS_dispatch_queue) -> ()
0x1946e3c24  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.setTargetQueue(__C.OS_dispatch_queue) -> ()
0x1946dc110  __TEXT,__text  XPC.XPCSession.debugDescription.getter : Swift.String
0x1946e2fa4  __TEXT,__const  property descriptor for XPC.XPCSession.debugDescription : Swift.String
0x1946dcc5c  __TEXT,__text  XPC.XPCSession.extractConnection() -> __C.OS_xpc_object
0x1946dcc8c  __TEXT,__text  XPC.XPCSession.setPeerRequirement(XPC.XPCPeerRequirement) -> ()
0x1946dcc80  __TEXT,__text  XPC.XPCSession.setTargetUserSession(userIdentifier: Swift.UInt32) -> ()
0x1946da1b0  __TEXT,__text  static XPC.XPCSession.InitializationOptions.privileged.getter : XPC.XPCSession.InitializationOptions
0x1946e2fa4  __TEXT,__const  property descriptor for static XPC.XPCSession.InitializationOptions.privileged : XPC.XPCSession.InitializationOptions
0x1946bf1e4  __TEXT,__text  static XPC.XPCSession.InitializationOptions.none.getter : XPC.XPCSession.InitializationOptions
0x1946e2fa4  __TEXT,__const  property descriptor for static XPC.XPCSession.InitializationOptions.none : XPC.XPCSession.InitializationOptions
0x1946da1a4  __TEXT,__text  static XPC.XPCSession.InitializationOptions.inactive.getter : XPC.XPCSession.InitializationOptions
0x1946e2fa4  __TEXT,__const  property descriptor for static XPC.XPCSession.InitializationOptions.inactive : XPC.XPCSession.InitializationOptions
0x1946da19c  __TEXT,__text  XPC.XPCSession.InitializationOptions.init(rawValue: Swift.UInt64) -> XPC.XPCSession.InitializationOptions
0x1946da194  __TEXT,__text  XPC.XPCSession.InitializationOptions.rawValue.getter : Swift.UInt64
0x1946e2fa0  __TEXT,__const  property descriptor for XPC.XPCSession.InitializationOptions.rawValue : Swift.UInt64
0x1946a904c  __TEXT,__text  type metadata accessor for XPC.XPCSession.InitializationOptions
0x1946e3c94  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCSession.InitializationOptions
0x1e38fec80  __AUTH_CONST,__const  type metadata for XPC.XPCSession.InitializationOptions
0x1946e2f20  __TEXT,__const  protocol conformance descriptor for XPC.XPCSession.InitializationOptions : Swift.Equatable in XPC
0x1946e2ee8  __TEXT,__const  protocol conformance descriptor for XPC.XPCSession.InitializationOptions : Swift.RawRepresentable in XPC
0x1946e2e20  __TEXT,__const  protocol conformance descriptor for XPC.XPCSession.InitializationOptions : Swift.SetAlgebra in XPC
0x1946e2f48  __TEXT,__const  protocol conformance descriptor for XPC.XPCSession.InitializationOptions : Swift.ExpressibleByArrayLiteral in XPC
0x1946e2de8  __TEXT,__const  protocol conformance descriptor for XPC.XPCSession.InitializationOptions : Swift.OptionSet in XPC
0x1946a8840  __TEXT,__text  dispatch thunk of XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> ()
0x1946e3c1c  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> ()
0x1946a92e8  __TEXT,__text  dispatch thunk of XPC.XPCSession.setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> ()
0x1946e3bfc  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> ()
0x1946a8a04  __TEXT,__text  dispatch thunk of XPC.XPCSession.setIncomingMessageHandler((XPC.XPCReceivedMessage) -> Swift.Encodable?) -> ()
0x1946e3c14  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.setIncomingMessageHandler((XPC.XPCReceivedMessage) -> Swift.Encodable?) -> ()
0x1946c1e4c  __TEXT,__text  dispatch thunk of XPC.XPCSession.setIncomingMessageHandler<A where A: Swift.Decodable>((A) -> Swift.Encodable?) -> ()
0x1946e3c0c  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.setIncomingMessageHandler<A where A: Swift.Decodable>((A) -> Swift.Encodable?) -> ()
0x1946a9db8  __TEXT,__text  dispatch thunk of XPC.XPCSession.send(message: XPC.XPCDictionary, replyHandler: (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> ()) -> ()
0x1946e3c74  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.send(message: XPC.XPCDictionary, replyHandler: (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> ()) -> ()
0x1946a9c04  __TEXT,__text  dispatch thunk of XPC.XPCSession.send(message: XPC.XPCDictionary) throws -> ()
0x1946e3c44  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.send(message: XPC.XPCDictionary) throws -> ()
0x1946a8b30  __TEXT,__text  dispatch thunk of XPC.XPCSession.send<A where A: Swift.Encodable>(_: A, replyHandler: (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> ()) throws -> ()
0x1946e3c8c  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.send<A where A: Swift.Encodable>(_: A, replyHandler: (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> ()) throws -> ()
0x1946addb4  __TEXT,__text  dispatch thunk of XPC.XPCSession.send<A, B where A: Swift.Encodable, B: Swift.Decodable>(_: A, replyHandler: (Swift.Result<B, Swift.Error>) -> ()) throws -> ()
0x1946e3c84  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.send<A, B where A: Swift.Encodable, B: Swift.Decodable>(_: A, replyHandler: (Swift.Result<B, Swift.Error>) -> ()) throws -> ()
0x1946ddb4c  __TEXT,__text  XPC.XPCSession.send<A where A: Swift.Encodable>(_: A, userInfo: [Swift.CodingUserInfoKey : Any], replyHandler: @Sendable (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> ()) throws -> ()
0x1946a7ec0  __TEXT,__text  dispatch thunk of XPC.XPCSession.send<A where A: Swift.Encodable>(A) throws -> ()
0x1946e3c4c  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.send<A where A: Swift.Encodable>(A) throws -> ()
0x1946bcc0c  __TEXT,__text  dispatch thunk of XPC.XPCSession.cancel(reason: Swift.String) -> ()
0x1946e3c34  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.cancel(reason: Swift.String) -> ()
0x1946a86e0  __TEXT,__text  dispatch thunk of XPC.XPCSession.activate() throws -> ()
0x1946e3c2c  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.activate() throws -> ()
0x1946db200  __TEXT,__text  XPC.XPCSession.__allocating_init(endpoint: XPC.XPCEndpoint, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946db5f0  __TEXT,__text  XPC.XPCSession.__allocating_init(endpoint: XPC.XPCEndpoint, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((XPC.XPCDictionary) -> XPC.XPCDictionary?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946dbcd0  __TEXT,__text  XPC.XPCSession.__allocating_init(endpoint: XPC.XPCEndpoint, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((XPC.XPCReceivedMessage) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946dbb70  __TEXT,__text  XPC.XPCSession.__allocating_init<A where A: Swift.Decodable>(endpoint: XPC.XPCEndpoint, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, incomingMessageHandler: ((A) -> Swift.Encodable?)?, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946a8b68  __TEXT,__text  dispatch thunk of XPC.XPCSession.sendSync(message: XPC.XPCDictionary) throws -> XPC.XPCDictionary
0x1946e3c54  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.sendSync(message: XPC.XPCDictionary) throws -> XPC.XPCDictionary
0x1946a9aa0  __TEXT,__text  dispatch thunk of XPC.XPCSession.sendSync<A where A: Swift.Encodable>(A) throws -> XPC.XPCReceivedMessage
0x1946e3c64  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.sendSync<A where A: Swift.Encodable>(A) throws -> XPC.XPCReceivedMessage
0x1946ded54  __TEXT,__text  dispatch thunk of XPC.XPCSession.sendSync<A, B where A: Swift.Encodable, B: Swift.Decodable>(A) throws -> B
0x1946e3c5c  __TEXT,__constg_swiftt  method descriptor for XPC.XPCSession.sendSync<A, B where A: Swift.Encodable, B: Swift.Decodable>(A) throws -> B
0x1946a5140  __TEXT,__text  type metadata accessor for XPC.XPCSession
0x1ee082a08  __DATA_DIRTY,__data  metaclass for XPC.XPCSession
0x1946e3bb0  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCSession
0x1946e2fc0  __TEXT,__const  class metadata base offset for XPC.XPCSession
0x1946ded20  __TEXT,__text  method lookup function for XPC.XPCSession
0x1ee0823c8  __DATA_DIRTY,__data  type metadata for XPC.XPCSession
0x1946bcc58  __TEXT,__text  XPC.XPCSession.__deallocating_deinit
0x1946db1e0  __TEXT,__text  XPC.XPCSession.deinit
0x1946e2f78  __TEXT,__const  protocol conformance descriptor for XPC.XPCSession : Swift.CustomDebugStringConvertible in XPC
0x1946df974  __TEXT,__text  XPC.xpc_retain(__C.OS_xpc_object) -> __C.OS_xpc_object
0x1946d7118  __TEXT,__text  XPC.XPCEndpoint.debugDescription.getter : Swift.String
0x1946e2968  __TEXT,__const  property descriptor for XPC.XPCEndpoint.debugDescription : Swift.String
0x1946d707c  __TEXT,__text  static XPC.XPCEndpoint.== infix(XPC.XPCEndpoint, XPC.XPCEndpoint) -> Swift.Bool
0x1946d72f4  __TEXT,__text  XPC.XPCEndpoint.init(from: Swift.Decoder) throws -> XPC.XPCEndpoint
0x1946d709c  __TEXT,__text  XPC.XPCEndpoint.hash(into: inout Swift.Hasher) -> ()
0x1946d71fc  __TEXT,__text  XPC.XPCEndpoint.encode(to: Swift.Encoder) throws -> ()
0x1946d7058  __TEXT,__text  XPC.XPCEndpoint._endpoint.getter : __C.OS_xpc_object
0x1946e2968  __TEXT,__const  property descriptor for XPC.XPCEndpoint._endpoint : __C.OS_xpc_object
0x1946d70cc  __TEXT,__text  XPC.XPCEndpoint.hashValue.getter : Swift.Int
0x1946e2968  __TEXT,__const  property descriptor for XPC.XPCEndpoint.hashValue : Swift.Int
0x1946d76d4  __TEXT,__text  type metadata accessor for XPC.XPCEndpoint
0x1946e3990  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCEndpoint
0x1e38fec00  __AUTH_CONST,__const  type metadata for XPC.XPCEndpoint
0x1946e2940  __TEXT,__const  protocol conformance descriptor for XPC.XPCEndpoint : Swift.Encodable in XPC
0x1946e28b0  __TEXT,__const  protocol conformance descriptor for XPC.XPCEndpoint : Swift.Hashable in XPC
0x1946e2888  __TEXT,__const  protocol conformance descriptor for XPC.XPCEndpoint : Swift.Equatable in XPC
0x1946e2918  __TEXT,__const  protocol conformance descriptor for XPC.XPCEndpoint : Swift.Decodable in XPC
0x1946e28f0  __TEXT,__const  protocol conformance descriptor for XPC.XPCEndpoint : Swift.CustomDebugStringConvertible in XPC
0x1946d6ffc  __TEXT,__text  XPC.XPCEndpoint.init(__C.OS_xpc_object) -> XPC.XPCEndpoint
0x1946d8a34  __TEXT,__text  XPC.XPCListener.__allocating_init(targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) -> XPC.XPCListener
0x1946d902c  __TEXT,__text  dispatch thunk of XPC.XPCListener.__allocating_init(targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) -> XPC.XPCListener
0x1946e39e8  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.__allocating_init(targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) -> XPC.XPCListener
0x1946d8a9c  __TEXT,__text  XPC.XPCListener.init(targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) -> XPC.XPCListener
0x1946d8718  __TEXT,__text  XPC.XPCListener.targetQueue.getter : __C.OS_dispatch_queue?
0x1946e2b68  __TEXT,__const  property descriptor for XPC.XPCListener.targetQueue : __C.OS_dispatch_queue?
0x1946d8cc0  __TEXT,__text  XPC.XPCListener.debugDescription.getter : Swift.String
0x1946e2b64  __TEXT,__const  property descriptor for XPC.XPCListener.debugDescription : Swift.String
0x1946c1e68  __TEXT,__text  XPC.XPCListener.setPeerRequirement(XPC.XPCPeerRequirement) -> ()
0x1946d76f4  __TEXT,__text  static XPC.XPCListener.InitializationOptions.none.getter : XPC.XPCListener.InitializationOptions
0x1946e2b64  __TEXT,__const  property descriptor for static XPC.XPCListener.InitializationOptions.none : XPC.XPCListener.InitializationOptions
0x1946c2bd8  __TEXT,__text  static XPC.XPCListener.InitializationOptions.inactive.getter : XPC.XPCListener.InitializationOptions
0x1946e2b64  __TEXT,__const  property descriptor for static XPC.XPCListener.InitializationOptions.inactive : XPC.XPCListener.InitializationOptions
0x1946d76ec  __TEXT,__text  XPC.XPCListener.InitializationOptions.init(rawValue: Swift.UInt64) -> XPC.XPCListener.InitializationOptions
0x1946d76e4  __TEXT,__text  XPC.XPCListener.InitializationOptions.rawValue.getter : Swift.UInt64
0x1946e2b60  __TEXT,__const  property descriptor for XPC.XPCListener.InitializationOptions.rawValue : Swift.UInt64
0x1946c2bc8  __TEXT,__text  type metadata accessor for XPC.XPCListener.InitializationOptions
0x1946e3a08  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCListener.InitializationOptions
0x1e38feb80  __AUTH_CONST,__const  type metadata for XPC.XPCListener.InitializationOptions
0x1946e2ae0  __TEXT,__const  protocol conformance descriptor for XPC.XPCListener.InitializationOptions : Swift.Equatable in XPC
0x1946e2aa8  __TEXT,__const  protocol conformance descriptor for XPC.XPCListener.InitializationOptions : Swift.RawRepresentable in XPC
0x1946e29e0  __TEXT,__const  protocol conformance descriptor for XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946e2b08  __TEXT,__const  protocol conformance descriptor for XPC.XPCListener.InitializationOptions : Swift.ExpressibleByArrayLiteral in XPC
0x1946e29a8  __TEXT,__const  protocol conformance descriptor for XPC.XPCListener.InitializationOptions : Swift.OptionSet in XPC
0x1946ad20c  __TEXT,__text  XPC.XPCListener.IncomingSessionRequest.withUnsafeAuditToken<A>((__C.audit_token_t) throws -> A) throws -> A
0x1946d9074  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.accept(incomingMessageHandler: (XPC.XPCDictionary) -> XPC.XPCDictionary?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946e3aa8  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.accept(incomingMessageHandler: (XPC.XPCDictionary) -> XPC.XPCDictionary?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946d90ac  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.accept(incomingMessageHandler: (XPC.XPCReceivedMessage) -> Swift.Encodable?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946e3ab8  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.accept(incomingMessageHandler: (XPC.XPCReceivedMessage) -> Swift.Encodable?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946d9090  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.accept<A where A: Swift.Decodable>(incomingMessageHandler: (A) -> Swift.Encodable?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946e3ab0  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.accept<A where A: Swift.Decodable>(incomingMessageHandler: (A) -> Swift.Encodable?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946d90c8  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.accept(incomingMessageHandler: (XPC.XPCDictionary) -> XPC.XPCDictionary?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> (XPC.XPCListener.IncomingSessionRequest.Decision, XPC.XPCSession)
0x1946e3ad0  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.accept(incomingMessageHandler: (XPC.XPCDictionary) -> XPC.XPCDictionary?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> (XPC.XPCListener.IncomingSessionRequest.Decision, XPC.XPCSession)
0x1946d9100  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.accept(incomingMessageHandler: (XPC.XPCReceivedMessage) -> Swift.Encodable?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> (XPC.XPCListener.IncomingSessionRequest.Decision, XPC.XPCSession)
0x1946e3ae0  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.accept(incomingMessageHandler: (XPC.XPCReceivedMessage) -> Swift.Encodable?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> (XPC.XPCListener.IncomingSessionRequest.Decision, XPC.XPCSession)
0x1946d90e4  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.accept<A where A: Swift.Decodable>(incomingMessageHandler: (A) -> Swift.Encodable?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> (XPC.XPCListener.IncomingSessionRequest.Decision, XPC.XPCSession)
0x1946e3ad8  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.accept<A where A: Swift.Decodable>(incomingMessageHandler: (A) -> Swift.Encodable?, cancellationHandler: ((XPC.XPCRichError) -> ())?) -> (XPC.XPCListener.IncomingSessionRequest.Decision, XPC.XPCSession)
0x1946d911c  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCDictionary, A.Output == XPC.XPCDictionary>((XPC.XPCSession) -> A) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946e3ae8  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCDictionary, A.Output == XPC.XPCDictionary>((XPC.XPCSession) -> A) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946ad4e4  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCReceivedMessage, A.Output == Swift.Encodable>((XPC.XPCSession) -> A) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946e3af8  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCReceivedMessage, A.Output == Swift.Encodable>((XPC.XPCSession) -> A) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946d9138  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input: Swift.Decodable, A.Output == Swift.Encodable>((XPC.XPCSession) -> A) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946e3af0  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input: Swift.Decodable, A.Output == Swift.Encodable>((XPC.XPCSession) -> A) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946d9154  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest.reject(reason: Swift.String) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946e3b00  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest.reject(reason: Swift.String) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946c1330  __TEXT,__text  dispatch thunk of XPC.XPCListener.IncomingSessionRequest._accept((XPC.XPCSession) -> ()) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946e3ac8  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.IncomingSessionRequest._accept((XPC.XPCSession) -> ()) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946d9178  __TEXT,__text  type metadata accessor for XPC.XPCListener.IncomingSessionRequest.Decision
0x1946e3b08  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCListener.IncomingSessionRequest.Decision
0x1e38fea70  __AUTH_CONST,__const  type metadata for XPC.XPCListener.IncomingSessionRequest.Decision
0x1946d8d9c  __TEXT,__text  XPC.XPCListener.IncomingSessionRequest.satisfies(requirement: XPC.XPCPeerRequirement) -> Swift.Bool
0x1946a978c  __TEXT,__text  type metadata accessor for XPC.XPCListener.IncomingSessionRequest
0x1ee082570  __DATA_DIRTY,__data  metaclass for XPC.XPCListener.IncomingSessionRequest
0x1946e3a24  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCListener.IncomingSessionRequest
0x1946e2c08  __TEXT,__const  class metadata base offset for XPC.XPCListener.IncomingSessionRequest
0x1946d905c  __TEXT,__text  method lookup function for XPC.XPCListener.IncomingSessionRequest
0x1ee0822a0  __DATA_DIRTY,__data  type metadata for XPC.XPCListener.IncomingSessionRequest
0x1946ad8a0  __TEXT,__text  XPC.XPCListener.IncomingSessionRequest.__deallocating_deinit
0x1946d86f8  __TEXT,__text  XPC.XPCListener.IncomingSessionRequest.deinit
0x1946c1740  __TEXT,__text  dispatch thunk of XPC.XPCListener.setIncomingSessionHandler(@Sendable (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) -> ()
0x1946e39f0  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.setIncomingSessionHandler(@Sendable (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) -> ()
0x1946d9040  __TEXT,__text  dispatch thunk of XPC.XPCListener.cancel() -> ()
0x1946e3a00  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.cancel() -> ()
0x1946c27fc  __TEXT,__text  XPC.XPCListener.__allocating_init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, requirement: XPC.XPCPeerRequirement, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) thro
0x1946d8740  __TEXT,__text  XPC.XPCListener.__allocating_init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) throws -> XPC.XPCListener
0x1946d9004  __TEXT,__text  dispatch thunk of XPC.XPCListener.__allocating_init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) throws -> XPC.XPCListen
0x1946e39e0  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.__allocating_init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) throws -> XPC.XPCLi
0x1946beb64  __TEXT,__text  XPC.XPCListener.init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) throws -> XPC.XPCListener
0x1946c123c  __TEXT,__text  dispatch thunk of XPC.XPCListener.activate() throws -> ()
0x1946e39f8  __TEXT,__constg_swiftt  method descriptor for XPC.XPCListener.activate() throws -> ()
0x1946d8c58  __TEXT,__text  XPC.XPCListener.endpoint.getter : XPC.XPCEndpoint
0x1946e2b64  __TEXT,__const  property descriptor for XPC.XPCListener.endpoint : XPC.XPCEndpoint
0x1946c2768  __TEXT,__text  type metadata accessor for XPC.XPCListener
0x1ee082598  __DATA_DIRTY,__data  metaclass for XPC.XPCListener
0x1946e39ac  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCListener
0x1946e2b90  __TEXT,__const  class metadata base offset for XPC.XPCListener
0x1946d8fec  __TEXT,__text  method lookup function for XPC.XPCListener
0x1ee082200  __DATA_DIRTY,__data  type metadata for XPC.XPCListener
0x1946d8c24  __TEXT,__text  XPC.XPCListener.__deallocating_deinit
0x1946d8bfc  __TEXT,__text  XPC.XPCListener.deinit
0x1946e2b38  __TEXT,__const  protocol conformance descriptor for XPC.XPCListener : Swift.CustomDebugStringConvertible in XPC
0x1946df9d0  __TEXT,__text  XPC.xpc_release(__C.OS_xpc_object) -> ()
0x1946da164  __TEXT,__text  XPC.XPCRichError.debugDescription.getter : Swift.String
0x1946e2d80  __TEXT,__const  property descriptor for XPC.XPCRichError.debugDescription : Swift.String
0x1946da15c  __TEXT,__text  XPC.XPCRichError.canRetry.getter : Swift.Bool
0x1946e2d80  __TEXT,__const  property descriptor for XPC.XPCRichError.canRetry : Swift.Bool
0x1946a89e4  __TEXT,__text  type metadata accessor for XPC.XPCRichError
0x1946e3b94  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCRichError
0x1e38fe9f0  __AUTH_CONST,__const  type metadata for XPC.XPCRichError
0x1946e2d18  __TEXT,__const  protocol conformance descriptor for XPC.XPCRichError : Swift.Error in XPC
0x1946e2d58  __TEXT,__const  protocol conformance descriptor for XPC.XPCRichError : Swift.CustomDebugStringConvertible in XPC
0x1946d57bc  __TEXT,__text  XPC.XPCDictionary.auditToken.getter : __C.audit_token_t
0x1946e2670  __TEXT,__const  property descriptor for XPC.XPCDictionary.auditToken : __C.audit_token_t
0x1946d561c  __TEXT,__text  XPC.XPCDictionary.createReply() -> XPC.XPCDictionary?
0x1946d4f54  __TEXT,__text  XPC.XPCDictionary.removeValue(forKey: Swift.String) -> __C.OS_xpc_object?
0x1946d5770  __TEXT,__text  XPC.XPCDictionary.debugDescription.getter : Swift.String
0x1946e2670  __TEXT,__const  property descriptor for XPC.XPCDictionary.debugDescription : Swift.String
0x1946d6cf4  __TEXT,__text  XPC.XPCDictionary.init(dictionaryLiteral: (Swift.String, XPC.XPCLiteralValue)...) -> XPC.XPCDictionary
0x1946d56d4  __TEXT,__text  static XPC.XPCDictionary.== infix(XPC.XPCDictionary, XPC.XPCDictionary) -> Swift.Bool
0x1946a8d98  __TEXT,__text  XPC.XPCDictionary.withUnsafeUnderlyingDictionary<A>((__C.OS_xpc_object) throws -> A) throws -> A
0x1946d52bc  __TEXT,__text  XPC.XPCDictionary.map<A>(((key: Swift.String, value: __C.OS_xpc_object)) throws -> A) throws -> [A]
0x1946d4e10  __TEXT,__text  XPC.XPCDictionary.copy(into: XPC.XPCDictionary) -> ()
0x1946d56f4  __TEXT,__text  XPC.XPCDictionary.hash(into: inout Swift.Hasher) -> ()
0x1946d556c  __TEXT,__text  XPC.XPCDictionary.keys.getter : [Swift.String]
0x1946e2670  __TEXT,__const  property descriptor for XPC.XPCDictionary.keys : [Swift.String]
0x1946d5020  __TEXT,__text  XPC.XPCDictionary.count.getter : Swift.Int
0x1946e2670  __TEXT,__const  property descriptor for XPC.XPCDictionary.count : Swift.Int
0x1946d568c  __TEXT,__text  XPC.XPCDictionary.reply(XPC.XPCDictionary) -> ()
0x1946b7340  __TEXT,__text  XPC.XPCDictionary.decode<A where A: Swift.Decodable>(as: A.Type, forKey: Swift.String, withUserInfo: [Swift.CodingUserInfoKey : Any]) throws -> A
0x1946d5820  __TEXT,__text  XPC.XPCDictionary.decode<A where A: Swift.Decodable>(as: A.Type, forKey: Swift.String) throws -> A
0x1946a8204  __TEXT,__text  XPC.XPCDictionary.encode<A where A: Swift.Encodable>(_: A, forKey: Swift.String, withUserInfo: [Swift.CodingUserInfoKey : Any]) throws -> ()
0x1946d58c8  __TEXT,__text  XPC.XPCDictionary.encode<A where A: Swift.Encodable>(_: A, forKey: Swift.String) throws -> ()
0x1946d55b4  __TEXT,__text  XPC.XPCDictionary.values.getter : [__C.OS_xpc_object]
0x1946e2670  __TEXT,__const  property descriptor for XPC.XPCDictionary.values : [__C.OS_xpc_object]
0x1946d5028  __TEXT,__text  XPC.XPCDictionary.forEach(((key: Swift.String, value: __C.OS_xpc_object)) throws -> ()) throws -> ()
0x1946a9338  __TEXT,__text  XPC.XPCDictionary.forEach((Swift.String, __C.OS_xpc_object) throws -> ()) throws -> ()
0x1946d4ffc  __TEXT,__text  XPC.XPCDictionary.isEmpty.getter : Swift.Bool
0x1946e2670  __TEXT,__const  property descriptor for XPC.XPCDictionary.isEmpty : Swift.Bool
0x1946b72f4  __TEXT,__text  XPC.XPCDictionary.contains(key: Swift.String) -> Swift.Bool
0x1946d5724  __TEXT,__text  XPC.XPCDictionary.hashValue.getter : Swift.Int
0x1946e2670  __TEXT,__const  property descriptor for XPC.XPCDictionary.hashValue : Swift.Int
0x1946d5684  __TEXT,__text  XPC.XPCDictionary.sendReply() -> ()
0x1946d21a0  __TEXT,__text  XPC.XPCDictionary.init() -> XPC.XPCDictionary
0x1946a903c  __TEXT,__text  type metadata accessor for XPC.XPCDictionary
0x1946e3958  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCDictionary
0x1e38fe7a0  __AUTH_CONST,__const  type metadata for XPC.XPCDictionary
0x1946e2608  __TEXT,__const  protocol conformance descriptor for XPC.XPCDictionary : Swift.Hashable in XPC
0x1946e25e0  __TEXT,__const  protocol conformance descriptor for XPC.XPCDictionary : Swift.Equatable in XPC
0x1946d42ec  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: System.FileDescriptor.Type) -> System.FileDescriptor?
0x1946d454c  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: System.FileDescriptor.Type, default: @autoclosure () -> System.FileDescriptor) -> System.FileDescriptor
0x1946d47f0  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: XPC.XPCArray.Type, default: @autoclosure () -> XPC.XPCArray) -> XPC.XPCArray
0x1946d23fc  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: Swift.Bool.Type, default: @autoclosure () -> Swift.Bool) -> Swift.Bool
0x1946d4290  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8).Type, default: @autoclosure () -
0x1946d3218  __TEXT,__text  XPC.XPCDictionary.subscript.getter : <A where A: Swift.BinaryFloatingPoint>(_: Swift.String, as: A.Type, default: @autoclosure () -> A) -> A
0x1946d4908  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: XPC.XPCEndpoint.Type) -> XPC.XPCEndpoint?
0x1946b42ec  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: XPC.XPCArray.Type) -> XPC.XPCArray?
0x1946b7538  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: XPC.XPCDictionary.Type) -> XPC.XPCDictionary?
0x1946b409c  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: Swift.String.Type) -> Swift.String?
0x1946d3708  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: [Swift.UInt8].Type) -> [Swift.UInt8]?
0x1946d21c8  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: Swift.Bool.Type) -> Swift.Bool?
0x1946d2490  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: __C.OS_xpc_object.Type) -> __C.OS_xpc_object?
0x1946d21cc  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: Swift.OpaquePointer) -> __C.OS_xpc_object?
0x1946e2670  __TEXT,__const  property descriptor for XPC.XPCDictionary.subscript(_: Swift.String, as: Swift.OpaquePointer) -> __C.OS_xpc_object?
0x1946d3e30  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8).Type) -> (Swift.UInt8, Swift.UIn
0x1946d33a4  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: Swift.RawSpan.Type) -> Swift.RawSpan?
0x1946d2cf0  __TEXT,__text  XPC.XPCDictionary.subscript.getter : <A where A: Swift.BinaryFloatingPoint>(_: Swift.String, as: A.Type) -> A?
0x1946b6ee4  __TEXT,__text  XPC.XPCDictionary.subscript.getter : <A where A: Swift.BinaryInteger>(_: Swift.String, as: A.Type) -> A?
0x1946e2648  __TEXT,__const  protocol conformance descriptor for XPC.XPCDictionary : Swift.CustomDebugStringConvertible in XPC
0x1946e2818  __TEXT,__const  protocol conformance descriptor for XPC.XPCDictionary : Swift.ExpressibleByDictionaryLiteral in XPC
0x1946d448c  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> System.FileDescriptor?
0x1946d4308  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> System.FileDescriptor?
0x1e0b855d4  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript(Swift.String) -> System.FileDescriptor?
0x1946d4340  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> System.FileDescriptor?
0x1946d4a58  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> XPC.XPCEndpoint?
0x1946d62ec  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> XPC.XPCEndpoint?
0x1e0b85628  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript(Swift.String) -> XPC.XPCEndpoint?
0x1946d49ec  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> XPC.XPCEndpoint?
0x1946d46c4  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> XPC.XPCArray?
0x1946d4630  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> XPC.XPCArray?
0x1e0b8560c  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript(Swift.String) -> XPC.XPCArray?
0x1946ac33c  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> XPC.XPCArray?
0x1946d45b0  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> XPC.XPCDictionary?
0x1946c1b80  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> XPC.XPCDictionary?
0x1e0b855f0  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript(Swift.String) -> XPC.XPCDictionary?
0x1946b4e50  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> XPC.XPCDictionary?
0x1946d2160  __TEXT,__text  XPC.XPCDictionary.init(__C.OS_xpc_object) -> XPC.XPCDictionary
0x1946d3d08  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> Swift.String?
0x1946d3a18  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> Swift.String?
0x1e0b8559c  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript(Swift.String) -> Swift.String?
0x1946d3aa8  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> Swift.String?
0x1946d3918  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> [Swift.UInt8]?
0x1946d62f0  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> [Swift.UInt8]?
0x1e0b85580  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript(Swift.String) -> [Swift.UInt8]?
0x1946d379c  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> [Swift.UInt8]?
0x1946d22e0  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> Swift.Bool?
0x1946c1e7c  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> Swift.Bool?
0x1e0b85510  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript(Swift.String) -> Swift.Bool?
0x1946d228c  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> Swift.Bool?
0x1946d4cb4  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> __C.OS_xpc_object?
0x1946c1bb4  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> __C.OS_xpc_object?
0x1e0b85644  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript(Swift.String) -> __C.OS_xpc_object?
0x1946ac4b4  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> __C.OS_xpc_object?
0x1946d4188  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)?
0x1946d3e34  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)?
0x1e0b855b8  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript(Swift.String) -> (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)?
0x1946d3e84  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)?
0x1946d3600  __TEXT,__text  XPC.XPCDictionary.subscript.modify : (Swift.String) -> Swift.RawSpan?
0x1946d346c  __TEXT,__text  XPC.XPCDictionary.subscript.getter : (Swift.String) -> Swift.RawSpan?
0x1946d3484  __TEXT,__text  XPC.XPCDictionary.subscript.setter : (Swift.String) -> Swift.RawSpan?
0x1946d2fec  __TEXT,__text  XPC.XPCDictionary.subscript.modify : <A where A: Swift.BinaryFloatingPoint>(Swift.String) -> A?
0x1946d2e6c  __TEXT,__text  XPC.XPCDictionary.subscript.getter : <A where A: Swift.BinaryFloatingPoint>(Swift.String) -> A?
0x1e0b85564  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript<A where A: Swift.BinaryFloatingPoint>(Swift.String) -> A?
0x1946d2ea8  __TEXT,__text  XPC.XPCDictionary.subscript.setter : <A where A: Swift.BinaryFloatingPoint>(Swift.String) -> A?
0x1946d2a70  __TEXT,__text  XPC.XPCDictionary.subscript.modify : <A where A: Swift.UnsignedInteger>(Swift.String) -> A?
0x1946b7264  __TEXT,__text  XPC.XPCDictionary.subscript.getter : <A where A: Swift.UnsignedInteger>(Swift.String) -> A?
0x1e0b85548  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript<A where A: Swift.UnsignedInteger>(Swift.String) -> A?
0x1946b6894  __TEXT,__text  XPC.XPCDictionary.subscript.setter : <A where A: Swift.UnsignedInteger>(Swift.String) -> A?
0x1946d2928  __TEXT,__text  XPC.XPCDictionary.subscript.modify : <A where A: Swift.SignedInteger>(Swift.String) -> A?
0x1946d62e8  __TEXT,__text  XPC.XPCDictionary.subscript.getter : <A where A: Swift.SignedInteger>(Swift.String) -> A?
0x1e0b8552c  __DATA_CONST,__const  property descriptor for XPC.XPCDictionary.subscript<A where A: Swift.SignedInteger>(Swift.String) -> A?
0x1946d2494  __TEXT,__text  XPC.XPCDictionary.subscript.setter : <A where A: Swift.SignedInteger>(Swift.String) -> A?
0x1946e3b24  __TEXT,__constg_swiftt  protocol descriptor for XPC.XPCPeerHandler
0x1946d919c  __TEXT,__text  dispatch thunk of XPC.XPCPeerHandler.handleCancellation(error: XPC.XPCRichError) -> ()
0x1946e3b54  __TEXT,__constg_swiftt  method descriptor for XPC.XPCPeerHandler.handleCancellation(error: XPC.XPCRichError) -> ()
0x1946d9188  __TEXT,__text  dispatch thunk of XPC.XPCPeerHandler.handleIncomingRequest(A.Input) -> A.Output?
0x1946e3b4c  __TEXT,__constg_swiftt  method descriptor for XPC.XPCPeerHandler.handleIncomingRequest(A.Input) -> A.Output?
0x1946d8cbc  __TEXT,__text  (extension in XPC):XPC.XPCPeerHandler.handleCancellation(error: XPC.XPCRichError) -> ()
0x1946e3b34  __TEXT,__constg_swiftt  protocol requirements base descriptor for XPC.XPCPeerHandler
0x1946d6ca0  __TEXT,__text  XPC.XPCLiteralValue.init(floatLiteral: Swift.Double) -> XPC.XPCLiteralValue
0x1946d6bf0  __TEXT,__text  XPC.XPCLiteralValue.init(stringLiteral: Swift.String) -> XPC.XPCLiteralValue
0x1946d6c48  __TEXT,__text  XPC.XPCLiteralValue.init(booleanLiteral: Swift.Bool) -> XPC.XPCLiteralValue
0x1946d6bf4  __TEXT,__text  XPC.XPCLiteralValue.init(integerLiteral: Swift.Int) -> XPC.XPCLiteralValue
0x1946d6fe4  __TEXT,__text  type metadata accessor for XPC.XPCLiteralValue
0x1946e3974  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCLiteralValue
0x1e38fe670  __AUTH_CONST,__const  type metadata for XPC.XPCLiteralValue
0x1946e27e0  __TEXT,__const  protocol conformance descriptor for XPC.XPCLiteralValue : Swift.ExpressibleByFloatLiteral in XPC
0x1946e26b8  __TEXT,__const  protocol conformance descriptor for XPC.XPCLiteralValue : Swift.ExpressibleByStringLiteral in XPC
0x1946e27a8  __TEXT,__const  protocol conformance descriptor for XPC.XPCLiteralValue : Swift.ExpressibleByBooleanLiteral in XPC
0x1946e2770  __TEXT,__const  protocol conformance descriptor for XPC.XPCLiteralValue : Swift.ExpressibleByIntegerLiteral in XPC
0x1946e2738  __TEXT,__const  protocol conformance descriptor for XPC.XPCLiteralValue : Swift.ExpressibleByUnicodeScalarLiteral in XPC
0x1946e26f8  __TEXT,__const  protocol conformance descriptor for XPC.XPCLiteralValue : Swift.ExpressibleByExtendedGraphemeClusterLiteral in XPC
0x1946d6300  __TEXT,__text  XPC.XPCLiteralValue.init(Swift.String) -> XPC.XPCLiteralValue
0x1946d6ff4  __TEXT,__text  XPC.XPCLiteralValue.init(Swift.Bool) -> XPC.XPCLiteralValue
0x1946d62f8  __TEXT,__text  XPC.XPCLiteralValue.init(__C.OS_xpc_object) -> XPC.XPCLiteralValue
0x1946d6ad8  __TEXT,__text  XPC.XPCLiteralValue.init<A where A: Swift.BinaryFloatingPoint>(A) -> XPC.XPCLiteralValue
0x1946d6774  __TEXT,__text  XPC.XPCLiteralValue.init<A where A: Swift.UnsignedInteger>(A) -> XPC.XPCLiteralValue
0x1946d637c  __TEXT,__text  XPC.XPCLiteralValue.init<A where A: Swift.SignedInteger>(A) -> XPC.XPCLiteralValue
0x1946d6be4  __TEXT,__text  XPC.XPCLiteralValue.init(XPC.XPCDictionary) -> XPC.XPCLiteralValue
0x1946d1f3c  __TEXT,__text  XPC.XPCCodableObject.debugDescription.getter : Swift.String
0x1946e2550  __TEXT,__const  property descriptor for XPC.XPCCodableObject.debugDescription : Swift.String
0x1946d1e7c  __TEXT,__text  XPC.XPCCodableObject.copyUnderlyingXPCObject() -> __C.OS_xpc_object
0x1946d1ea0  __TEXT,__text  static XPC.XPCCodableObject.== infix(XPC.XPCCodableObject, XPC.XPCCodableObject) -> Swift.Bool
0x1946bd22c  __TEXT,__text  XPC.XPCCodableObject.init(from: Swift.Decoder) throws -> XPC.XPCCodableObject
0x1946d1ec0  __TEXT,__text  XPC.XPCCodableObject.hash(into: inout Swift.Hasher) -> ()
0x1946d1e74  __TEXT,__text  XPC.XPCCodableObject.type.getter : Swift.OpaquePointer
0x1946e2550  __TEXT,__const  property descriptor for XPC.XPCCodableObject.type : Swift.OpaquePointer
0x1946bd6d8  __TEXT,__text  XPC.XPCCodableObject.encode(to: Swift.Encoder) throws -> ()
0x1946c03fc  __TEXT,__text  XPC.XPCCodableObject.init(copying: __C.OS_xpc_object) -> XPC.XPCCodableObject
0x1946d1ef0  __TEXT,__text  XPC.XPCCodableObject.hashValue.getter : Swift.Int
0x1946e2550  __TEXT,__const  property descriptor for XPC.XPCCodableObject.hashValue : Swift.Int
0x1946c1320  __TEXT,__text  type metadata accessor for XPC.XPCCodableObject
0x1946e390c  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCCodableObject
0x1e38fe5e0  __AUTH_CONST,__const  type metadata for XPC.XPCCodableObject
0x1946e2528  __TEXT,__const  protocol conformance descriptor for XPC.XPCCodableObject : Swift.Encodable in XPC
0x1946e2498  __TEXT,__const  protocol conformance descriptor for XPC.XPCCodableObject : Swift.Hashable in XPC
0x1946e2470  __TEXT,__const  protocol conformance descriptor for XPC.XPCCodableObject : Swift.Equatable in XPC
0x1946e2500  __TEXT,__const  protocol conformance descriptor for XPC.XPCCodableObject : Swift.Decodable in XPC
0x1946e24d8  __TEXT,__const  protocol conformance descriptor for XPC.XPCCodableObject : Swift.CustomDebugStringConvertible in XPC
0x1946c9c60  __TEXT,__text  XPC.XPCEncodedContents.init(value: Swift.Encodable, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> XPC.XPCEncodedContents
0x1946c3758  __TEXT,__text  default argument 1 of XPC.XPCEncodedContents.init(value: Swift.Encodable, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> XPC.XPCEncodedContents
0x1946caf70  __TEXT,__text  XPC.XPCEncodedContents.decode<A where A: Swift.Decodable>(as: A.Type, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> A
0x1946c3764  __TEXT,__text  default argument 1 of XPC.XPCEncodedContents.decode<A where A: Swift.Decodable>(as: A.Type, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> A
0x1946cb174  __TEXT,__text  type metadata accessor for XPC.XPCEncodedContents
0x1946e3454  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCEncodedContents
0x1e38fe348  __AUTH_CONST,__const  type metadata for XPC.XPCEncodedContents
0x1946d978c  __TEXT,__text  static XPC.XPCPeerRequirement.entitlement(_: Swift.String, matches: Swift.String) -> XPC.XPCPeerRequirement
0x1946d9574  __TEXT,__text  static XPC.XPCPeerRequirement.entitlement(_: Swift.String, matches: Swift.Bool) -> XPC.XPCPeerRequirement
0x1946d9964  __TEXT,__text  static XPC.XPCPeerRequirement.entitlement(_: Swift.String, matches: Swift.Int) -> XPC.XPCPeerRequirement
0x1946d9dd8  __TEXT,__text  static XPC.XPCPeerRequirement.fromLWCRData(Swift.UnsafeRawBufferPointer) -> XPC.XPCPeerRequirement
0x1946bb350  __TEXT,__text  static XPC.XPCPeerRequirement.hasEntitlement(Swift.String) -> XPC.XPCPeerRequirement
0x1946d9b28  __TEXT,__text  static XPC.XPCPeerRequirement.isFromSameTeam(andMatchesSigningIdentifier: Swift.String?) -> XPC.XPCPeerRequirement
0x1946d9ba4  __TEXT,__text  static XPC.XPCPeerRequirement.isPlatformCode(andMatchesSigningIdentifier: Swift.String?) -> XPC.XPCPeerRequirement
0x1946d9fc0  __TEXT,__text  XPC.XPCPeerRequirement.init(lightweightCodeRequirements: XPC.XPCDictionary) -> XPC.XPCPeerRequirement
0x1946c2624  __TEXT,__text  type metadata accessor for XPC.XPCPeerRequirement
0x1946e3b78  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCPeerRequirement
0x1e38fe2c8  __AUTH_CONST,__const  type metadata for XPC.XPCPeerRequirement
0x1946b5c98  __TEXT,__text  XPC.XPCReceivedMessage.auditToken.getter : __C.audit_token_t
0x1946e3240  __TEXT,__const  property descriptor for XPC.XPCReceivedMessage.auditToken : __C.audit_token_t
0x1946e01bc  __TEXT,__text  XPC.XPCReceivedMessage.init(dictionary: XPC.XPCDictionary) -> XPC.XPCReceivedMessage
0x1946e027c  __TEXT,__text  XPC.XPCReceivedMessage.expectsReply.getter : Swift.Bool
0x1946e3240  __TEXT,__const  property descriptor for XPC.XPCReceivedMessage.expectsReply : Swift.Bool
0x1946b5b80  __TEXT,__text  XPC.XPCReceivedMessage.handoffReply(to: __C.OS_dispatch_queue, _: () -> ()) -> Swift.Encodable?
0x1946e02a4  __TEXT,__text  XPC.XPCReceivedMessage.detachHandoff() -> ()
0x1946e02b0  __TEXT,__text  XPC.XPCReceivedMessage.senderSatisfies(XPC.XPCPeerRequirement) -> Swift.Bool
0x1946b5d74  __TEXT,__text  XPC.XPCReceivedMessage.reply<A where A: Swift.Encodable>(_: A, userInfo: [Swift.CodingUserInfoKey : Any]) -> ()
0x1946b5cfc  __TEXT,__text  XPC.XPCReceivedMessage.reply<A where A: Swift.Encodable>(A) -> ()
0x1946ac99c  __TEXT,__text  XPC.XPCReceivedMessage.decode<A where A: Swift.Decodable>(as: A.Type, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> A
0x1946c3770  __TEXT,__text  default argument 0 of XPC.XPCReceivedMessage.decode<A where A: Swift.Decodable>(as: A.Type, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> A
0x1946b3550  __TEXT,__text  XPC.XPCReceivedMessage.decode<A where A: Swift.Decodable>(as: A.Type) throws -> A
0x1946e0298  __TEXT,__text  XPC.XPCReceivedMessage.isSync.getter : Swift.Bool
0x1946e3240  __TEXT,__const  property descriptor for XPC.XPCReceivedMessage.isSync : Swift.Bool
0x1946a89f4  __TEXT,__text  type metadata accessor for XPC.XPCReceivedMessage
0x1946e3d18  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCReceivedMessage
0x1e38fe248  __AUTH_CONST,__const  type metadata for XPC.XPCReceivedMessage
0x1946df458  __TEXT,__text  XPC.xpc_session_cancel(__C.OS_xpc_object) -> ()
0x1946df7d4  __TEXT,__text  XPC.xpc_listener_cancel(__C.OS_xpc_listener) -> ()
0x1946df634  __TEXT,__text  XPC.xpc_listener_create(Swift.UnsafePointer<Swift.Int8>, __C.OS_dispatch_queue?, XPC.xpc_listener_create_flags_t, (__C.OS_xpc_object) -> (), Swift.AutoreleasingUnsafeMutablePointer<__C.OS_xpc_object?>?) -> __C.OS_xpc_listener?
0x1946df440  __TEXT,__text  XPC.xpc_session_activate(__C.OS_xpc_object, Swift.AutoreleasingUnsafeMutablePointer<__C.OS_xpc_object?>?) -> Swift.Bool
0x1946df704  __TEXT,__text  XPC.xpc_listener_activate(__C.OS_xpc_listener, Swift.AutoreleasingUnsafeMutablePointer<__C.OS_xpc_object?>?) -> Swift.Bool
0x1946c85e4  __TEXT,__text  XPC.testEncodeDecodePipeline<A where A: Swift.Decodable, A: Swift.Encodable>(_: A, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> A
0x1946df8a4  __TEXT,__text  XPC.xpc_listener_reject_peer(__C.OS_xpc_object, Swift.UnsafePointer<Swift.Int8>) -> ()
0x1946df45c  __TEXT,__text  XPC.xpc_session_send_message(__C.OS_xpc_object, __C.OS_xpc_object) -> __C.OS_xpc_object?
0x1946a8174  __TEXT,__text  type metadata accessor for XPC.TopLevelGraphEncodingNode
0x1ee0829c8  __DATA_DIRTY,__data  metaclass for XPC.TopLevelGraphEncodingNode
0x1946e33f0  __TEXT,__constg_swiftt  nominal type descriptor for XPC.TopLevelGraphEncodingNode
0x1946e1460  __TEXT,__const  class metadata base offset for XPC.TopLevelGraphEncodingNode
0x1946cb0d8  __TEXT,__text  method lookup function for XPC.TopLevelGraphEncodingNode
0x1ee081eb0  __DATA_DIRTY,__data  type metadata for XPC.TopLevelGraphEncodingNode
0x1946ac608  __TEXT,__text  XPC.TopLevelGraphEncodingNode.__deallocating_deinit
0x1946c857c  __TEXT,__text  XPC.TopLevelGraphEncodingNode.deinit
0x1946c9ad8  __TEXT,__text  XPC.encodeToEncodingContainer<A where A: Swift.Encodable>(_: A, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> XPC.TopLevelGraphEncodingNode
0x1946df224  __TEXT,__text  static XPC.xpc_session_create_flags_t.privileged.getter : XPC.xpc_session_create_flags_t
0x1946e31a0  __TEXT,__const  property descriptor for static XPC.xpc_session_create_flags_t.privileged : XPC.xpc_session_create_flags_t
0x1946df21c  __TEXT,__text  static XPC.xpc_session_create_flags_t.none.getter : XPC.xpc_session_create_flags_t
0x1946e31a0  __TEXT,__const  property descriptor for static XPC.xpc_session_create_flags_t.none : XPC.xpc_session_create_flags_t
0x1946df230  __TEXT,__text  static XPC.xpc_session_create_flags_t.inactive.getter : XPC.xpc_session_create_flags_t
0x1946e31a0  __TEXT,__const  property descriptor for static XPC.xpc_session_create_flags_t.inactive : XPC.xpc_session_create_flags_t
0x1946df214  __TEXT,__text  XPC.xpc_session_create_flags_t.init(rawValue: Swift.UInt64) -> XPC.xpc_session_create_flags_t
0x1946df20c  __TEXT,__text  XPC.xpc_session_create_flags_t.rawValue.getter : Swift.UInt64
0x1946e31a0  __TEXT,__const  property descriptor for XPC.xpc_session_create_flags_t.rawValue : Swift.UInt64
0x1946dfb64  __TEXT,__text  type metadata accessor for XPC.xpc_session_create_flags_t
0x1946e3cb0  __TEXT,__constg_swiftt  nominal type descriptor for XPC.xpc_session_create_flags_t
0x1e38fdd78  __AUTH_CONST,__const  type metadata for XPC.xpc_session_create_flags_t
0x1946e3148  __TEXT,__const  protocol conformance descriptor for XPC.xpc_session_create_flags_t : Swift.Equatable in XPC
0x1946e3110  __TEXT,__const  protocol conformance descriptor for XPC.xpc_session_create_flags_t : Swift.RawRepresentable in XPC
0x1946e3048  __TEXT,__const  protocol conformance descriptor for XPC.xpc_session_create_flags_t : Swift.SetAlgebra in XPC
0x1946e3170  __TEXT,__const  protocol conformance descriptor for XPC.xpc_session_create_flags_t : Swift.ExpressibleByArrayLiteral in XPC
0x1946e3010  __TEXT,__const  protocol conformance descriptor for XPC.xpc_session_create_flags_t : Swift.OptionSet in XPC
0x1946c9bb4  __TEXT,__text  XPC.decodeFromEncodingContainer<A where A: Swift.Decodable>(_: A.Type, from: XPC.TopLevelGraphEncodingNode, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> A
0x1946dfc44  __TEXT,__text  type metadata accessor for XPC.xpc_listener_create_flags_t
0x1946e3ccc  __TEXT,__constg_swiftt  nominal type descriptor for XPC.xpc_listener_create_flags_t
0x1e38fdd00  __AUTH_CONST,__const  type metadata for XPC.xpc_listener_create_flags_t
0x1946df208  __TEXT,__text  XPC.xpc_session_copy_description(__C.OS_xpc_object) -> Swift.UnsafeMutablePointer<Swift.Int8>?
0x1946df43c  __TEXT,__text  XPC.xpc_session_set_target_queue(__C.OS_xpc_object, __C.OS_dispatch_queue?) -> ()
0x1946e3928  __TEXT,__constg_swiftt  protocol descriptor for XPC.XPCCodableObjectRepresentable
0x1946d2138  __TEXT,__text  dispatch thunk of XPC.XPCCodableObjectRepresentable.xpcCodableObject.getter : XPC.XPCCodableObject
0x1946e3948  __TEXT,__constg_swiftt  method descriptor for XPC.XPCCodableObjectRepresentable.xpcCodableObject.getter : XPC.XPCCodableObject
0x1946d214c  __TEXT,__text  dispatch thunk of static XPC.XPCCodableObjectRepresentable.validXPCObjectTypes.getter : Swift.Set<Swift.OpaquePointer>
0x1946e3950  __TEXT,__constg_swiftt  method descriptor for static XPC.XPCCodableObjectRepresentable.validXPCObjectTypes.getter : Swift.Set<Swift.OpaquePointer>
0x1946d2124  __TEXT,__text  dispatch thunk of XPC.XPCCodableObjectRepresentable.init(from: XPC.XPCCodableObject) -> A?
0x1946e3940  __TEXT,__constg_swiftt  method descriptor for XPC.XPCCodableObjectRepresentable.init(from: XPC.XPCCodableObject) -> A?
0x1946d200c  __TEXT,__text  static (extension in XPC):XPC.XPCCodableObjectRepresentable.validXPCObjectTypes.getter : Swift.Set<Swift.OpaquePointer>
0x1946e2550  __TEXT,__const  property descriptor for static (extension in XPC):XPC.XPCCodableObjectRepresentable.validXPCObjectTypes : Swift.Set<Swift.OpaquePointer>
0x1946e3938  __TEXT,__constg_swiftt  protocol requirements base descriptor for XPC.XPCCodableObjectRepresentable
0x1946df564  __TEXT,__text  XPC.xpc_listener_copy_description(__C.OS_xpc_listener) -> Swift.UnsafeMutablePointer<Swift.Int8>?
0x1946df35c  __TEXT,__text  XPC.xpc_session_set_cancel_handler(__C.OS_xpc_object, (__C.OS_xpc_object) -> ()) -> ()
0x1946df2bc  __TEXT,__text  XPC.xpc_session_create_mach_service(Swift.UnsafePointer<Swift.Int8>, __C.OS_dispatch_queue?, XPC.xpc_session_create_flags_t, Swift.AutoreleasingUnsafeMutablePointer<__C.OS_xpc_object?>?) -> __C.OS_xpc_object?
0x1946df47c  __TEXT,__text  XPC.xpc_session_send_message_with_reply_sync(__C.OS_xpc_object, __C.OS_xpc_object, Swift.AutoreleasingUnsafeMutablePointer<__C.OS_xpc_object?>?) -> __C.OS_xpc_object?
0x1946df33c  __TEXT,__text  XPC.xpc_session_set_incoming_message_handler(__C.OS_xpc_object, (__C.OS_xpc_object) -> ()) -> ()
0x1946c8714  __TEXT,__text  XPC.testEncodeDecodePipelineWithSerialization<A where A: Swift.Decodable, A: Swift.Encodable>(_: A, userInfo: [Swift.CodingUserInfoKey : Any]) throws -> A
0x1946df49c  __TEXT,__text  XPC.xpc_session_send_message_with_reply_async(__C.OS_xpc_object, __C.OS_xpc_object, (__C.OS_xpc_object?, __C.OS_xpc_object?) -> ()) -> ()
0x1946d1b98  __TEXT,__text  XPC.XPCArray.debugDescription.getter : Swift.String
0x1946e2430  __TEXT,__const  property descriptor for XPC.XPCArray.debugDescription : Swift.String
0x1946ce664  __TEXT,__text  XPC.XPCArray.withUnsafeUnderlyingArray<A>((__C.OS_xpc_object) throws -> A) throws -> A
0x1946d1a38  __TEXT,__text  static XPC.XPCArray.== infix(XPC.XPCArray, XPC.XPCArray) -> Swift.Bool
0x1946d1828  __TEXT,__text  XPC.XPCArray.map<A>(((index: Swift.Int, value: __C.OS_xpc_object)) throws -> A) throws -> [A]
0x1946d15d8  __TEXT,__text  XPC.XPCArray.copy(into: XPC.XPCArray) -> ()
0x1946d1a58  __TEXT,__text  XPC.XPCArray.hash(into: inout Swift.Hasher) -> ()
0x1946ce554  __TEXT,__text  XPC.XPCArray.count.getter : Swift.Int
0x1946e2430  __TEXT,__const  property descriptor for XPC.XPCArray.count : Swift.Int
0x1946d1740  __TEXT,__text  XPC.XPCArray.forEach(((index: Swift.Int, value: __C.OS_xpc_object)) throws -> ()) throws -> ()
0x1946c1be8  __TEXT,__text  XPC.XPCArray.forEach((Swift.Int, __C.OS_xpc_object) throws -> ()) throws -> ()
0x1946d171c  __TEXT,__text  XPC.XPCArray.isEmpty.getter : Swift.Bool
0x1946e2430  __TEXT,__const  property descriptor for XPC.XPCArray.isEmpty : Swift.Bool
0x1946d1a88  __TEXT,__text  XPC.XPCArray.hashValue.getter : Swift.Int
0x1946e2430  __TEXT,__const  property descriptor for XPC.XPCArray.hashValue : Swift.Int
0x1946ce5fc  __TEXT,__text  XPC.XPCArray.init() -> XPC.XPCArray
0x1946d1e2c  __TEXT,__text  type metadata accessor for XPC.XPCArray
0x1946e38f0  __TEXT,__constg_swiftt  nominal type descriptor for XPC.XPCArray
0x1e38fd9d0  __AUTH_CONST,__const  type metadata for XPC.XPCArray
0x1946e23c8  __TEXT,__const  protocol conformance descriptor for XPC.XPCArray : Swift.Hashable in XPC
0x1946e23a0  __TEXT,__const  protocol conformance descriptor for XPC.XPCArray : Swift.Equatable in XPC
0x1946d0ac4  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: System.FileDescriptor.Type) -> System.FileDescriptor?
0x1946d0b94  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: System.FileDescriptor.Type, default: @autoclosure () -> System.FileDescriptor) -> System.FileDescriptor
0x1946d1304  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: XPC.XPCEndpoint.Type, default: @autoclosure () -> XPC.XPCEndpoint) -> XPC.XPCEndpoint
0x1946d0fe8  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: XPC.XPCArray.Type, default: @autoclosure () -> XPC.XPCArray) -> XPC.XPCArray
0x1946cec00  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: Swift.Bool.Type, default: @autoclosure () -> Swift.Bool) -> Swift.Bool
0x1946d0954  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8).Type, default: @autoclosure () -> (Swift
0x1946d0024  __TEXT,__text  XPC.XPCArray.subscript.getter : <A where A: Swift.BinaryFloatingPoint>(_: Swift.Int, as: A.Type, default: @autoclosure () -> A) -> A
0x1946d1074  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: XPC.XPCEndpoint.Type) -> XPC.XPCEndpoint?
0x1946d0be0  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: XPC.XPCDictionary.Type) -> XPC.XPCDictionary?
0x1946d0df4  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: XPC.XPCArray.Type) -> XPC.XPCArray?
0x1946d03b0  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: Swift.String.Type) -> Swift.String?
0x1946ce694  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: Swift.Bool.Type) -> Swift.Bool?
0x1946cec90  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: __C.OS_xpc_object.Type) -> __C.OS_xpc_object?
0x1946ce708  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: Swift.OpaquePointer) -> __C.OS_xpc_object?
0x1946e2430  __TEXT,__const  property descriptor for XPC.XPCArray.subscript(_: Swift.Int, as: Swift.OpaquePointer) -> __C.OS_xpc_object?
0x1946d05c4  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8).Type) -> (Swift.UInt8, Swift.UInt8, Swif
0x1946d01b0  __TEXT,__text  XPC.XPCArray.subscript.getter : (_: Swift.Int, as: Swift.RawSpan.Type) -> Swift.RawSpan?
0x1946cfa8c  __TEXT,__text  XPC.XPCArray.subscript.getter : <A where A: Swift.BinaryFloatingPoint>(_: Swift.Int, as: A.Type) -> A?
0x1946c20c4  __TEXT,__text  XPC.XPCArray.subscript.getter : <A where A: Swift.BinaryInteger>(_: Swift.Int, as: A.Type) -> A?
0x1946e2408  __TEXT,__const  protocol conformance descriptor for XPC.XPCArray : Swift.CustomDebugStringConvertible in XPC
0x1946d0b18  __TEXT,__text  XPC.XPCArray.subscript.modify : (Swift.Int) -> System.FileDescriptor?
0x1946d1e3c  __TEXT,__text  XPC.XPCArray.subscript.getter : (Swift.Int) -> System.FileDescriptor?
0x1e0b85480  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript(Swift.Int) -> System.FileDescriptor?
0x1946d0af8  __TEXT,__text  XPC.XPCArray.subscript.setter : (Swift.Int) -> System.FileDescriptor?
0x1946d1180  __TEXT,__text  XPC.XPCArray.subscript.modify : (Swift.Int) -> XPC.XPCEndpoint?
0x1946d1e68  __TEXT,__text  XPC.XPCArray.subscript.getter : (Swift.Int) -> XPC.XPCEndpoint?
0x1e0b854d4  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript(Swift.Int) -> XPC.XPCEndpoint?
0x1946d10f0  __TEXT,__text  XPC.XPCArray.subscript.setter : (Swift.Int) -> XPC.XPCEndpoint?
0x1946d0d10  __TEXT,__text  XPC.XPCArray.subscript.modify : (Swift.Int) -> XPC.XPCDictionary?
0x1946d1e60  __TEXT,__text  XPC.XPCArray.subscript.getter : (Swift.Int) -> XPC.XPCDictionary?
0x1e0b8549c  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript(Swift.Int) -> XPC.XPCDictionary?
0x1946d0ccc  __TEXT,__text  XPC.XPCArray.subscript.setter : (Swift.Int) -> XPC.XPCDictionary?
0x1946d0f54  __TEXT,__text  XPC.XPCArray.subscript.modify : (Swift.Int) -> XPC.XPCArray?
0x1946d1e64  __TEXT,__text  XPC.XPCArray.subscript.getter : (Swift.Int) -> XPC.XPCArray?
0x1e0b854b8  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript(Swift.Int) -> XPC.XPCArray?
0x1946d0ee0  __TEXT,__text  XPC.XPCArray.subscript.setter : (Swift.Int) -> XPC.XPCArray?
0x1946ce624  __TEXT,__text  XPC.XPCArray.init(__C.OS_xpc_object) -> XPC.XPCArray
0x1946d04f8  __TEXT,__text  XPC.XPCArray.subscript.modify : (Swift.Int) -> Swift.String?
0x1946d1e58  __TEXT,__text  XPC.XPCArray.subscript.getter : (Swift.Int) -> Swift.String?
0x1e0b85448  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript(Swift.Int) -> Swift.String?
0x1946d0428  __TEXT,__text  XPC.XPCArray.subscript.setter : (Swift.Int) -> Swift.String?
0x1946ceae8  __TEXT,__text  XPC.XPCArray.subscript.modify : (Swift.Int) -> Swift.Bool?
0x1946ce8ec  __TEXT,__text  XPC.XPCArray.subscript.getter : (Swift.Int) -> Swift.Bool?
0x1e0b853d8  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript(Swift.Int) -> Swift.Bool?
0x1946cea60  __TEXT,__text  XPC.XPCArray.subscript.setter : (Swift.Int) -> Swift.Bool?
0x1946d1500  __TEXT,__text  XPC.XPCArray.subscript.modify : (Swift.Int) -> __C.OS_xpc_object?
0x1946ce55c  __TEXT,__text  XPC.XPCArray.subscript.getter : (Swift.Int) -> __C.OS_xpc_object?
0x1e0b854f0  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript(Swift.Int) -> __C.OS_xpc_object?
0x1946ce584  __TEXT,__text  XPC.XPCArray.subscript.setter : (Swift.Int) -> __C.OS_xpc_object?
0x1946d07cc  __TEXT,__text  XPC.XPCArray.subscript.modify : (Swift.Int) -> (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)?
0x1946d05c8  __TEXT,__text  XPC.XPCArray.subscript.getter : (Swift.Int) -> (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)?
0x1e0b85464  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript(Swift.Int) -> (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)?
0x1946d06f0  __TEXT,__text  XPC.XPCArray.subscript.setter : (Swift.Int) -> (Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8, Swift.UInt8)?
0x1946d02e0  __TEXT,__text  XPC.XPCArray.subscript.modify : (Swift.Int) -> Swift.RawSpan?
0x1946d027c  __TEXT,__text  XPC.XPCArray.subscript.getter : (Swift.Int) -> Swift.RawSpan?
0x1946d02b0  __TEXT,__text  XPC.XPCArray.subscript.setter : (Swift.Int) -> Swift.RawSpan?
0x1946cfe50  __TEXT,__text  XPC.XPCArray.subscript.modify : <A where A: Swift.BinaryFloatingPoint>(Swift.Int) -> A?
0x1946cfc0c  __TEXT,__text  XPC.XPCArray.subscript.getter : <A where A: Swift.BinaryFloatingPoint>(Swift.Int) -> A?
0x1e0b8542c  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript<A where A: Swift.BinaryFloatingPoint>(Swift.Int) -> A?
0x1946cfc48  __TEXT,__text  XPC.XPCArray.subscript.setter : <A where A: Swift.BinaryFloatingPoint>(Swift.Int) -> A?
0x1946cf894  __TEXT,__text  XPC.XPCArray.subscript.modify : <A where A: Swift.UnsignedInteger>(Swift.Int) -> A?
0x1946c1e10  __TEXT,__text  XPC.XPCArray.subscript.getter : <A where A: Swift.UnsignedInteger>(Swift.Int) -> A?
0x1e0b85410  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript<A where A: Swift.UnsignedInteger>(Swift.Int) -> A?
0x1946cf35c  __TEXT,__text  XPC.XPCArray.subscript.setter : <A where A: Swift.UnsignedInteger>(Swift.Int) -> A?
0x1946cf14c  __TEXT,__text  XPC.XPCArray.subscript.modify : <A where A: Swift.SignedInteger>(Swift.Int) -> A?
0x1946c1e0c  __TEXT,__text  XPC.XPCArray.subscript.getter : <A where A: Swift.SignedInteger>(Swift.Int) -> A?
0x1e0b853f4  __DATA_CONST,__const  property descriptor for XPC.XPCArray.subscript<A where A: Swift.SignedInteger>(Swift.Int) -> A?
0x1946cecb8  __TEXT,__text  XPC.XPCArray.subscript.setter : <A where A: Swift.SignedInteger>(Swift.Int) -> A?
0x1946e3b3c  __TEXT,__constg_swiftt  associated type descriptor for XPC.XPCPeerHandler.Input
0x1946e3b44  __TEXT,__constg_swiftt  associated type descriptor for XPC.XPCPeerHandler.Output
0x1946cd08c  __TEXT,__text  (extension in XPC):Swift.Encodable.encodeAsXPCObject(withUserInfo: [Swift.CodingUserInfoKey : Any]) throws -> __C.OS_xpc_object
0x1946dfde4  __TEXT,__text  (extension in XPC):Swift.Array<A where A == Swift.UInt8>.byteDescription.getter : Swift.String
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):Swift.Array<A where A == Swift.UInt8>.byteDescription : Swift.String
0x1946cd0c8  __TEXT,__text  (extension in XPC):__C.OS_xpc_object.decode<A where A1: Swift.Decodable>(as: A1.Type, withUserInfo: [Swift.CodingUserInfoKey : Any]) throws -> A1
0x1946dffb4  __TEXT,__text  (extension in XPC):__C.audit_token_t.fromSameProcessAs(__C.audit_token_t) -> Swift.Bool
0x1946dff9c  __TEXT,__text  (extension in XPC):__C.audit_token_t.pid.getter : Swift.UInt32
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):__C.audit_token_t.pid : Swift.UInt32
0x1946dffa4  __TEXT,__text  (extension in XPC):__C.audit_token_t.asid.getter : Swift.UInt32
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):__C.audit_token_t.asid : Swift.UInt32
0x1946dff78  __TEXT,__text  (extension in XPC):__C.audit_token_t.auid.getter : Swift.UInt32
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):__C.audit_token_t.auid : Swift.UInt32
0x1946dff84  __TEXT,__text  (extension in XPC):__C.audit_token_t.egid.getter : Swift.UInt32
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):__C.audit_token_t.egid : Swift.UInt32
0x1946dff7c  __TEXT,__text  (extension in XPC):__C.audit_token_t.euid.getter : Swift.UInt32
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):__C.audit_token_t.euid : Swift.UInt32
0x1946dff94  __TEXT,__text  (extension in XPC):__C.audit_token_t.rgid.getter : Swift.UInt32
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):__C.audit_token_t.rgid : Swift.UInt32
0x1946dff8c  __TEXT,__text  (extension in XPC):__C.audit_token_t.ruid.getter : Swift.UInt32
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):__C.audit_token_t.ruid : Swift.UInt32
0x1946dffac  __TEXT,__text  (extension in XPC):__C.audit_token_t.execcnt.getter : Swift.UInt32
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):__C.audit_token_t.execcnt : Swift.UInt32
0x1946dffd0  __TEXT,__text  (extension in XPC):__C.audit_token_t.isValid.getter : Swift.Bool
0x1946e3218  __TEXT,__const  property descriptor for (extension in XPC):__C.audit_token_t.isValid : Swift.Bool
0x1946bb508  __TEXT,__text  (extension in XPC):__C.audit_token_t.satisfies(requirement: XPC.XPCPeerRequirement) -> Swift.Bool
0x1946cd498  __TEXT,__text  static (extension in XPC):Swift.CodingUserInfoKey.xpcCodable.getter : Swift.CodingUserInfoKey
0x1eb9af718  __DATA,__common  __swift_FORCE_LOAD_$_swiftXPC
```

## Private

```
0x1946a5130  __TEXT,__text  one-time initialization function for inactive
0x1946a5164  __TEXT,__text  XPC.ClientSpecifiedHandler.init((A) -> B) -> XPC.ClientSpecifiedHandler<A, B>
0x1946a51b8  __TEXT,__text  ___swift_instantiateConcreteTypeFromMangledNameV2
0x1946a5658  __TEXT,__text  outlined copy of (@escaping @callee_guaranteed @Sendable (@in_guaranteed XPC.XPCRichError) -> ())?
0x1946a5670  __TEXT,__text  __swift__xpc_session_create_from_connection_4SWIFT
0x1946a56d8  __TEXT,__text  XPC.XPCSession.setIncomingMessageHandler((XPC.XPCReceivedMessage) -> Swift.Encodable?) -> ()
0x1946a5858  __TEXT,__text  _block_copy_helper.48
0x1946a585c  __TEXT,__text  _block_copy_helper
0x1946a586c  __TEXT,__text  _block_copy_helper
0x1946a587c  __TEXT,__text  _block_copy_helper
0x1946a588c  __TEXT,__text  _block_copy_helper
0x1946a589c  __TEXT,__text  _block_copy_helper
0x1946a58ac  __TEXT,__text  _block_copy_helper
0x1946a58bc  __TEXT,__text  __swift_xpc_session_set_cancel_handler
0x1946a590c  __TEXT,__text  __swift_xpc_session_set_cancel_handler
0x1946a595c  __TEXT,__text  XPC.XPCSession.activate() throws -> ()
0x1946a5ab0  __TEXT,__text  __swift_xpc_session_set_incoming_message_handler
0x1946a5b00  __TEXT,__text  __swift_xpc_session_set_incoming_message_handler
0x1946a5b50  __TEXT,__text  XPC.XPCSession.send<A where A: Swift.Encodable>(A) throws -> ()
0x1946a5c9c  __TEXT,__text  _block_copy_helper.171
0x1946a5ca0  __TEXT,__text  __swift_xpc_session_activate
0x1946a5ca0  __TEXT,__text  __swift_xpc_session_activate
0x1946a5cdc  __TEXT,__text  generic specialization <Swift.CodingUserInfoKey, Any> of Swift._NativeDictionary._insert(at: Swift._HashTable.Bucket, key: __owned A, value: __owned B) -> ()
0x1946a5da4  __TEXT,__text  generic specialization <Swift.CodingUserInfoKey> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(A) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x1946a5dfc  __TEXT,__text  generic specialization <Swift.CodingUserInfoKey> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(_: A, hashValue: Swift.Int) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x1946a5f78  __TEXT,__text  generic specialization <Swift.CodingUserInfoKey, Any> of Swift._NativeDictionary.setValue(_: __owned B, forKey: A, isUnique: Swift.Bool) -> ()
0x1946a612c  __TEXT,__text  static XPC.XPCReceivedMessage.encodeMessage<A where A: Swift.Encodable>(_: A, userInfo: [Swift.CodingUserInfoKey : Any], isSync: Swift.Bool) throws -> XPC.XPCDictionary
0x1946a771c  __TEXT,__text  ___swift_project_value_buffer
0x1946a7740  __TEXT,__text  outlined init with copy of Any
0x1946a7794  __TEXT,__text  ___swift_destroy_boxed_opaque_existential_1
0x1946a7794  __TEXT,__text  ___swift_destroy_boxed_opaque_existential_1
0x1946a77c4  __TEXT,__text  outlined init with take of Any
0x1946a77d4  __TEXT,__text  lazy protocol witness table accessor for type XPC._TopLevelEncoder and conformance XPC._TopLevelEncoder : Swift.Encoder in XPC
0x1946a7828  __TEXT,__text  one-time initialization function for xpcCodable
0x1946a7948  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <Swift.CodingUserInfoKey, Any> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x1946a7ae0  __TEXT,__text  ___swift_allocate_value_buffer
0x1946a7b30  __TEXT,__text  generic specialization <Swift.CodingUserInfoKey, Any> of Swift._NativeDictionary._copyOrMoveAndResize(capacity: Swift.Int, moveElements: Swift.Bool) -> ()
0x1946a7ef0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7ef0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7ef0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7ef0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7ef0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7ef0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7f34  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7f34  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7f34  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7f34  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7f34  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7f34  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCArray
0x1946a7f70  __TEXT,__text  ___swift_closure_destructor.3
0x1946a7f74  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed (@unowned Swift.UnsafePointer<Swift.Int8>, @guaranteed __C.OS_xpc_object) -> (@unowned Swift.Bool) to @callee_unowned @convention(block) (@unowned Swift.UnsafePointer<Swift.Int8>, @unowned __C.OS_xpc_object) -> (@unowned Swift.Bool)
0x1946a7fcc  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@unowned Swift.UnsafePointer<Swift.Int8>, @guaranteed __C.OS_xpc_object) -> (@unowned Swift.Bool) to @escaping @callee_guaranteed (@unowned Swift.UnsafePointer<Swift.Int8>, @guaranteed __C.OS_xpc_object) -> (@unowned Swi
0x1946a7ff8  __TEXT,__text  ___swift_memcpy8_8
0x1946a8004  __TEXT,__text  ___swift_closure_destructor
0x1946a8030  __TEXT,__text  ___swift_closure_destructor
0x1946a805c  __TEXT,__text  ___swift_closure_destructor
0x1946a8088  __TEXT,__text  ___swift_closure_destructor
0x1946a80b4  __TEXT,__text  _block_destroy_helper
0x1946a80bc  __TEXT,__text  _block_destroy_helper
0x1946a80c4  __TEXT,__text  _block_destroy_helper
0x1946a80cc  __TEXT,__text  _block_destroy_helper
0x1946a80d4  __TEXT,__text  _block_destroy_helper
0x1946a80dc  __TEXT,__text  _block_destroy_helper
0x1946a80e4  __TEXT,__text  ___swift_closure_destructor.14
0x1946a80f4  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafePointer<Swift.Int8>, __C.OS_xpc_object) -> Swift.Bool in XPC.XPCDictionary.copy(into: XPC.XPCDictionary) -> ()
0x1946a811c  __TEXT,__text  __swift_xpc_session_send_message
0x1946a81bc  __TEXT,__text  merged XPC.XPC_ERROR_KEY_DESCRIPTION.getter : Swift.UnsafePointer<Swift.Int8>
0x1946a828c  __TEXT,__text  function signature specialization <Arg[4] = Dead> of XPC.XPCSession.__allocating_init(machService: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCSession.InitializationOptions, cancellationHandler: ((XPC.XPCRichError) -> ())?) throws -> XPC.XPCSession
0x1946a8684  __TEXT,__text  __swift_xpc_session_create_mach_service
0x1946a8710  __TEXT,__text  XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> ()
0x1946a885c  __TEXT,__text  _block_copy_helper.59
0x1946a8860  __TEXT,__text  XPC.XPCSession._send<A where A: Swift.Encodable>(_: A, replyHandler: (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> ()) throws -> ()
0x1946a8a20  __TEXT,__text  XPC.XPCSession.send<A where A: Swift.Encodable>(_: A, replyHandler: (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> ()) throws -> ()
0x1946a8b98  __TEXT,__text  __swift_xpc_session_send_message_with_reply_sync
0x1946a8b98  __TEXT,__text  __swift_xpc_session_send_message_with_reply_sync
0x1946a8bf8  __TEXT,__text  XPC.XPCSession.sendSync(message: XPC.XPCDictionary) throws -> XPC.XPCDictionary
0x1946a8d78  __TEXT,__text  ___swift_closure_destructor.63
0x1946a8d7c  __TEXT,__text  ___swift_closure_destructor.63
0x1946a8d80  __TEXT,__text  outlined consume of Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>
0x1946a8dc8  __TEXT,__text  partial apply forwarder for implicit closure #2 (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> () in implicit closure #1 (XPC.ClientSpecifiedHandler<Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>, ()>) -> (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> () in XPC.XPCSession.send(mes
0x1946a8df4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ())
0x1946a8dfc  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ())
0x1946a8dfc  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ())
0x1946a8e24  __TEXT,__text  closure #1 (__C.OS_xpc_object?, __C.OS_xpc_object?) -> () in XPC.XPCSession._send(message: XPC.XPCDictionary, replyHandler: (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> ()) -> ()
0x1946a8f50  __TEXT,__text  merged implicit closure #2 (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> () in implicit closure #1 (XPC.ClientSpecifiedHandler<Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>, ()>) -> (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> () in XPC.XPCSession.send(message: XPC.XPCDictiona
0x1946a8fc0  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object?, __C.OS_xpc_object?) -> () in XPC.XPCSession._send(message: XPC.XPCDictionary, replyHandler: (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> ()) -> ()
0x1946a8fc8  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed __C.OS_xpc_object?, @guaranteed __C.OS_xpc_object?) -> () to @escaping @callee_unowned @convention(block) (@unowned __C.OS_xpc_object?, @unowned __C.OS_xpc_object?) -> ()
0x1946a9030  __TEXT,__text  ___swift_closure_destructor.69
0x1946a9034  __TEXT,__text  ___swift_closure_destructor.66
0x1946a9038  __TEXT,__text  _block_destroy_helper.72
0x1946a905c  __TEXT,__text  base witness table accessor for Swift.Equatable in XPC.XPCSession.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a9060  __TEXT,__text  lazy protocol witness table accessor for type XPC.XPCSession.InitializationOptions and conformance XPC.XPCSession.InitializationOptions : Swift.Equatable in XPC
0x1946a90b4  __TEXT,__text  lazy protocol witness table accessor for type XPC.XPCSession.InitializationOptions and conformance XPC.XPCSession.InitializationOptions : Swift.ExpressibleByArrayLiteral in XPC
0x1946a9108  __TEXT,__text  base witness table accessor for Swift.ExpressibleByArrayLiteral in XPC.XPCSession.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a910c  __TEXT,__text  protocol witness for Swift.SetAlgebra.init<A where A1: Swift.Sequence, A.Element == A1.Element>(__owned A1) -> A in conformance XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a910c  __TEXT,__text  protocol witness for Swift.SetAlgebra.init<A where A1: Swift.Sequence, A.Element == A1.Element>(__owned A1) -> A in conformance XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a910c  __TEXT,__text  protocol witness for Swift.SetAlgebra.init<A where A1: Swift.Sequence, A.Element == A1.Element>(__owned A1) -> A in conformance XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a9124  __TEXT,__text  protocol witness for Swift.SetAlgebra.init() -> A in conformance XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a9124  __TEXT,__text  protocol witness for Swift.SetAlgebra.init() -> A in conformance XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a9124  __TEXT,__text  protocol witness for Swift.SetAlgebra.init() -> A in conformance XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a912c  __TEXT,__text  ___swift_noop_void_return
0x1946a9130  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCListener.InitializationOptions
0x1946a9130  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCListener.InitializationOptions
0x1946a9130  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCListener.InitializationOptions
0x1946a9158  __TEXT,__text  protocol witness for Swift.SetAlgebra.insert(__owned A.Element) -> (inserted: Swift.Bool, memberAfterInsert: A.Element) in conformance XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a9158  __TEXT,__text  protocol witness for Swift.SetAlgebra.insert(__owned A.Element) -> (inserted: Swift.Bool, memberAfterInsert: A.Element) in conformance XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a9158  __TEXT,__text  protocol witness for Swift.SetAlgebra.insert(__owned A.Element) -> (inserted: Swift.Bool, memberAfterInsert: A.Element) in conformance XPC.XPCListener.InitializationOptions : Swift.SetAlgebra in XPC
0x1946a9178  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCListener.InitializationOptions
0x1946a9178  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCListener.InitializationOptions
0x1946a9178  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCListener.InitializationOptions
0x1946a9198  __TEXT,__text  XPC.XPCSession.setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> ()
0x1946a92e4  __TEXT,__text  _block_copy_helper.21
0x1946a9304  __TEXT,__text  _block_destroy_helper.79
0x1946a9308  __TEXT,__text  ___swift_closure_destructor.6
0x1946a930c  __TEXT,__text  ___swift_closure_destructor.72
0x1946a9410  __TEXT,__text  closure #1 ((Swift.String, __C.OS_xpc_object) throws -> ()) throws -> () in XPC.XPCDictionary.forEach((Swift.String, __C.OS_xpc_object) throws -> ()) throws -> ()
0x1946a9588  __TEXT,__text  _block_copy_helper.78
0x1946a958c  __TEXT,__text  ___swift_closure_destructor.75
0x1946a9590  __TEXT,__text  ___swift_closure_destructor.75
0x1946a95bc  __TEXT,__text  closure #1 (Swift.UnsafePointer<Swift.Int8>, __C.OS_xpc_object) -> Swift.Bool in closure #1 ((Swift.String, __C.OS_xpc_object) throws -> ()) throws -> () in XPC.XPCDictionary.forEach((Swift.String, __C.OS_xpc_object) throws -> ()) throws -> ()
0x1946a9638  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafePointer<Swift.Int8>, __C.OS_xpc_object) -> Swift.Bool in closure #1 ((Swift.String, __C.OS_xpc_object) throws -> ()) throws -> () in XPC.XPCDictionary.forEach((Swift.String, __C.OS_xpc_object) throws -> ()) throws -> ()
0x1946a9644  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@unowned Swift.UnsafePointer<Swift.Int8>, @guaranteed __C.OS_xpc_object) -> (@unowned Swift.Bool) to @escaping @callee_guaranteed (@unowned Swift.UnsafePointer<Swift.Int8>, @guaranteed __C.OS_xpc_object) -> (@unowned Swi
0x1946a9648  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error)
0x1946a9648  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error)
0x1946a9670  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed __C.OS_xpc_session) -> () to @escaping @callee_unowned @convention(block) (@unowned __C.OS_xpc_session) -> ()
0x1946a96c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_session) -> () in XPC.XPCListener.init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionReq
0x1946a96c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_session) -> () in XPC.XPCListener.init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionReq
0x1946a96c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_session) -> () in XPC.XPCListener.init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionReq
0x1946a96c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_session) -> () in XPC.XPCListener.init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionReq
0x1946a96c8  __TEXT,__text  merged closure #1 (__C.OS_xpc_session) -> () in XPC.XPCListener.init(service: Swift.String, targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) throws
0x1946a9770  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_session) -> () in XPC.XPCListener.init(targetQueue: __C.OS_dispatch_queue?, options: XPC.XPCListener.InitializationOptions, incomingSessionHandler: (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) -> XPC.X
0x1946a97b0  __TEXT,__text  merged partial apply forwarder for implicit closure #2 (XPC.XPCDictionary) -> XPC.XPCDictionary? in implicit closure #1 (XPC.ClientSpecifiedHandler<XPC.XPCDictionary, XPC.XPCDictionary?>) -> (XPC.XPCDictionary) -> XPC.XPCDictionary? in XPC.XPCSession.setIncomingMessageHandler((XPC.XPCDictionary) -> 
0x1946a9820  __TEXT,__text  partial apply forwarder for implicit closure #2 (XPC.XPCDictionary) -> XPC.XPCDictionary? in implicit closure #1 (XPC.ClientSpecifiedHandler<XPC.XPCDictionary, XPC.XPCDictionary?>) -> (XPC.XPCDictionary) -> XPC.XPCDictionary? in XPC.XPCSession.setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPC
0x1946a9828  __TEXT,__text  partial apply forwarder for implicit closure #2 (XPC.XPCDictionary) -> XPC.XPCDictionary? in implicit closure #1 (XPC.ClientSpecifiedHandler<XPC.XPCDictionary, XPC.XPCDictionary?>) -> (XPC.XPCDictionary) -> XPC.XPCDictionary? in XPC.XPCSession.setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPC
0x1946a982c  __TEXT,__text  closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> ()
0x1946a98dc  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> ()
0x1946a98e4  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed __C.OS_xpc_object) -> () to @escaping @callee_unowned @convention(block) (@unowned __C.OS_xpc_object) -> ()
0x1946a9930  __TEXT,__text  _block_copy_helper.256
0x1946a9934  __TEXT,__text  XPC.XPCSession.sendSync<A where A: Swift.Encodable>(A) throws -> XPC.XPCReceivedMessage
0x1946a9ad0  __TEXT,__text  XPC.ClientSpecifiedHandler.callEventHandler(A) -> B
0x1946a9b24  __TEXT,__text  XPC.XPCSession.send(message: XPC.XPCDictionary) throws -> ()
0x1946a9c34  __TEXT,__text  XPC.XPCSession.send(message: XPC.XPCDictionary, replyHandler: (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> ()) -> ()
0x1946a9dd4  __TEXT,__text  _block_copy_helper.71
0x1946a9dd8  __TEXT,__text  __swift_xpc_session_send_message_with_reply_async
0x1946a9e44  __TEXT,__text  ___swift_allocate_boxed_opaque_existential_1
0x1946a9e94  __TEXT,__text  XPC._KeyedGraphEncodingNode.(_valueIndex in _7E1E3A1581E9D210C0DAF0092A52A88E)(forKey: XPC.EncodingGraph.Key) -> Swift.Int?
0x1946a9fcc  __TEXT,__text  __swift_stdlib_malloc_size
0x1946a9fd0  __TEXT,__text  XPC._KeyedGraphEncodingNode.subscript.setter : (XPC.EncodingGraph.Key) -> XPC.EncodingGraph.Value?
0x1946aa268  __TEXT,__text  XPC._KeyedEncodingContainer.nestedContainer<A where A1: Swift.CodingKey>(keyedBy: A1.Type, forKey: A) -> Swift.KeyedEncodingContainer<A1>
0x1946aa42c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.nestedContainer<A where A1: Swift.CodingKey>(keyedBy: A1.Type, forKey: A.Key) -> Swift.KeyedEncodingContainer<A1> in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946aa468  __TEXT,__text  associated type witness table accessor for XPC._EncodingContainer.Container : XPC.EncodingGraph.Container in XPC._KeyedEncodingContainer<A> : XPC._EncodingContainer in XPC
0x1946aa474  __TEXT,__text  type metadata instantiation function for XPC._KeyedEncodingContainer
0x1946aa4b0  __TEXT,__text  type metadata completion function for XPC._KeyedDecodingContainer
0x1946aa4b0  __TEXT,__text  type metadata completion function for XPC._KeyedDecodingContainer
0x1946aa4bc  __TEXT,__text  type metadata instantiation function for XPC._KeyedEncodingContainer._ContainerCodingKey
0x1946aa4c4  __TEXT,__text  base witness table accessor for Swift.CustomDebugStringConvertible in XPC._KeyedEncodingContainer<A>._ContainerCodingKey : Swift.CodingKey in XPC
0x1946aa4e0  __TEXT,__text  type metadata completion function for XPC._KeyedEncodingContainer._ContainerCodingKey
0x1946aa53c  __TEXT,__text  base witness table accessor for Swift.CustomStringConvertible in XPC._KeyedEncodingContainer<A>._ContainerCodingKey : Swift.CodingKey in XPC
0x1946aa558  __TEXT,__text  XPC._TopLevelEncoder.container<A where A: Swift.CodingKey>(keyedBy: A.Type) -> Swift.KeyedEncodingContainer<A>
0x1946aa618  __TEXT,__text  XPC._TopLevelEncoder._encodingContainer<A where A: XPC._EncodingContainer>(A.Type) -> A
0x1946aa74c  __TEXT,__text  protocol witness for Swift.Encoder.container<A where A1: Swift.CodingKey>(keyedBy: A1.Type) -> Swift.KeyedEncodingContainer<A1> in conformance XPC._TopLevelEncoder : Swift.Encoder in XPC
0x1946aa760  __TEXT,__text  ___swift_instantiateGenericMetadata
0x1946aa790  __TEXT,__text  type metadata accessor for XPC._KeyedEncodingContainer
0x1946aa7a8  __TEXT,__text  XPC._KeyedEncodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container?) -> XPC._KeyedEncodingContainer<A>
0x1946aa848  __TEXT,__text  protocol witness for XPC._EncodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container?) -> A in conformance XPC._KeyedEncodingContainer<A> : XPC._EncodingContainer in XPC
0x1946aa874  __TEXT,__text  protocol witness for XPC._EncodingContainer.container.getter : A.Container in conformance XPC._KeyedEncodingContainer<A> : XPC._EncodingContainer in XPC
0x1946aa874  __TEXT,__text  protocol witness for XPC._EncodingContainer.container.getter : A.Container in conformance XPC._KeyedEncodingContainer<A> : XPC._EncodingContainer in XPC
0x1946aa874  __TEXT,__text  protocol witness for XPC._EncodingContainer.container.getter : A.Container in conformance XPC._KeyedEncodingContainer<A> : XPC._EncodingContainer in XPC
0x1946aa87c  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <XPC.EncodingGraph.Key, Swift.Int> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x1946aa988  __TEXT,__text  outlined destroy of Swift.CodingKey?
0x1946aa9e8  __TEXT,__text  type metadata accessor for XPC._KeyedGraphEncodingNode
0x1946aaa0c  __TEXT,__text  XPC.CodingInfo.coding(forKey: Swift.CodingKey?, forType: Any.Type?) -> XPC.CodingInfo
0x1946aaaf4  __TEXT,__text  XPC._KeyedEncodingContainer.(_existingNode in _7E1E3A1581E9D210C0DAF0092A52A88E)(forKey: XPC.EncodingGraph.Key) -> XPC.EncodingGraph.Container?
0x1946aaba4  __TEXT,__text  type metadata accessor for XPC._KeyedEncodingContainer._ContainerCodingKey
0x1946aabbc  __TEXT,__text  XPC._KeyedEncodingContainer.(_encodingContainer in _7E1E3A1581E9D210C0DAF0092A52A88E)<A where A1: XPC._EncodingContainer>(_: A1.Type, forKey: XPC._KeyedEncodingContainer<A>._ContainerCodingKey, forType: Any.Type?) -> A1
0x1946aadf0  __TEXT,__text  XPC._KeyedEncodingContainer._ContainerCodingKey.encodingGraphKey.getter : XPC.EncodingGraph.Key
0x1946aae90  __TEXT,__text  ___swift_memcpy32_8
0x1946aae9c  __TEXT,__text  generic specialization <Swift.CodingKey> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x1946aafd8  __TEXT,__text  outlined init with copy of Swift.CodingKey
0x1946aafd8  __TEXT,__text  outlined init with copy of Swift.CodingKey
0x1946ab034  __TEXT,__text  type metadata accessor for XPC.EncodingGraph.Key
0x1946ab044  __TEXT,__text  type metadata accessor for XPC.EncodingGraph.Value
0x1946ab054  __TEXT,__text  base witness table accessor for Swift.Equatable in XPC.EncodingGraph.Key : Swift.Hashable in XPC
0x1946ab058  __TEXT,__text  lazy protocol witness table accessor for type XPC.EncodingGraph.Key and conformance XPC.EncodingGraph.Key : Swift.Equatable in XPC
0x1946ab0ac  __TEXT,__text  generic specialization <Swift.OpaquePointer> of Swift.Set.contains(A) -> Swift.Bool
0x1946ab178  __TEXT,__text  _get_enum_tag_for_layout_string 3XPC13EncodingGraphO5ValueO
0x1946ab194  __TEXT,__text  XPC.XPCData.init(underlyingData: __C.OS_xpc_object) -> XPC.XPCData?
0x1946ab25c  __TEXT,__text  (extension in XPC):__C.OS_xpc_object.isCodable() -> Swift.Bool
0x1946ab2c0  __TEXT,__text  outlined consume of XPC.EncodingGraph.Value
0x1946ab304  __TEXT,__text  generic specialization <XPC.EncodingGraph.Value> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x1946ab408  __TEXT,__text  generic specialization <XPC.EncodingGraph.Key> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(A) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x1946ab490  __TEXT,__text  XPC._KeyedEncodingContainer.(_encode in _7E1E3A1581E9D210C0DAF0092A52A88E)(_: XPC.EncodingGraph.Value, forKey: XPC.EncodingGraph.Key) -> ()
0x1946ab51c  __TEXT,__text  generic specialization <XPC.EncodingGraph.Key, Swift.Int> of Swift._NativeDictionary.setValue(_: __owned B, forKey: A, isUnique: Swift.Bool) -> ()
0x1946ab670  __TEXT,__text  generic specialization <XPC.EncodingGraph.Key, Swift.Int> of Swift._NativeDictionary._copyOrMoveAndResize(capacity: Swift.Int, moveElements: Swift.Bool) -> ()
0x1946ab90c  __TEXT,__text  outlined copy of XPC.EncodingGraph.Value
0x1946ab950  __TEXT,__text  generic specialization <XPC.EncodingGraph.Key> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(_: A, hashValue: Swift.Int) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x1946aba1c  __TEXT,__text  ___swift_exist.box.addr_destructor
0x1946aba60  __TEXT,__text  ___swift_exist.box.addr_destructor
0x1946aba7c  __TEXT,__text  ___swift_exist.box.addr_destructor
0x1946aba80  __TEXT,__text  ___swift_exist.box.addr_destructor
0x1946aba88  __TEXT,__text  ___swift_exist.box.addr_destructor
0x1946abac4  __TEXT,__text  ___swift_exist.box.addr_destructor
0x1946abb00  __TEXT,__text  ___swift_exist.box.addr_destructor
0x1946abb3c  __TEXT,__text  ___swift_exist.box.addr_destructor
0x1946abb78  __TEXT,__text  ___swift_exist.box.addr_destructor
0x1946abbb4  __TEXT,__text  one-time initialization function for allTypes
0x1946abda4  __TEXT,__text  generic specialization <Swift.ObjectIdentifier, Swift.UInt32> of Swift._NativeDictionary._copyOrMoveAndResize(capacity: Swift.Int, moveElements: Swift.Bool) -> ()
0x1946abfe8  __TEXT,__text  generic specialization <XPC.EncodingGraph.Container> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x1946ac114  __TEXT,__text  generic specialization <Swift.ObjectIdentifier> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(A) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x1946ac14c  __TEXT,__text  init(firstPass: FirstPass #1 in XPC.SerializedEncodingGraph.init(of: XPC.EncodingGraph.Container) -> XPC.SerializedEncodingGraph) -> SecondPass #1 in XPC.SerializedEncodingGraph.init(of: XPC.EncodingGraph.Container) -> XPC.SerializedEncodingGraph in SecondPass #1 in XPC.SerializedEncodingGraph.init(
0x1946ac214  __TEXT,__text  outlined destroy of SecondPass #1 in XPC.SerializedEncodingGraph.init(of: XPC.EncodingGraph.Container) -> XPC.SerializedEncodingGraph
0x1946ac260  __TEXT,__text  outlined init with copy of SecondPass #1 in XPC.SerializedEncodingGraph.init(of: XPC.EncodingGraph.Container) -> XPC.SerializedEncodingGraph
0x1946ac2b4  __TEXT,__text  protocol witness for XPC.EncodingGraph.Container.values.getter : [XPC.EncodingGraph.Value] in conformance XPC.TopLevelGraphEncodingNode : XPC.EncodingGraph.Container in XPC
0x1946ac410  __TEXT,__text  generic specialization <Swift.ObjectIdentifier> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(_: A, hashValue: Swift.Int) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x1946ac47c  __TEXT,__text  protocol witness for XPC.EncodingGraph.Container.values.getter : [XPC.EncodingGraph.Value] in conformance XPC._KeyedGraphEncodingNode : XPC.EncodingGraph.Container in XPC
0x1946ac634  __TEXT,__text  XPC.XPCReceivedMessage.XPCReceivedMessageMetadata.__deallocating_deinit
0x1946ac644  __TEXT,__text  merged outlined destroy of Swift.CodingKey?
0x1946ac644  __TEXT,__text  merged outlined destroy of Swift.CodingKey?
0x1946ac644  __TEXT,__text  merged outlined destroy of Swift.CodingKey?
0x1946ac69c  __TEXT,__text  XPC._KeyedDecodingContainer.decode<A where A1: Swift.Decodable>(_: A1.Type, forKey: A) throws -> A1
0x1946ad144  __TEXT,__text  ___swift_exist.box.addr_destructor.5
0x1946ad14c  __TEXT,__text  ___swift_exist.box.addr_destructor.5
0x1946ad168  __TEXT,__text  ___swift_exist.box.addr_destructor.2Tm
0x1946ad168  __TEXT,__text  ___swift_exist.box.addr_destructor.2Tm
0x1946ad1b0  __TEXT,__text  XPC.SingleValueGraphEncodingNode.__deallocating_deinit
0x1946ad1b0  __TEXT,__text  XPC.SingleValueGraphEncodingNode.__deallocating_deinit
0x1946ad1b0  __TEXT,__text  XPC.SingleValueGraphEncodingNode.__deallocating_deinit
0x1946ad1dc  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC.XPCListener.IncomingSessionRequest.Decision) to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC
0x1946ad208  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC.XPCListener.IncomingSessionRequest.Decision) to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC
0x1946ad208  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC.XPCListener.IncomingSessionRequest.Decision) to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC
0x1946ad208  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC.XPCListener.IncomingSessionRequest.Decision) to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC
0x1946ad208  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC.XPCListener.IncomingSessionRequest.Decision) to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCListener.IncomingSessionRequest) -> (@out XPC
0x1946ad27c  __TEXT,__text  XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCReceivedMessage, A.Output == Swift.Encodable>((XPC.XPCSession) -> A) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946ad3d8  __TEXT,__text  implicit closure #1 (A) -> (XPC.XPCReceivedMessage) -> Swift.Encodable? in XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCReceivedMessage, A.Output == Swift.Encodable>((XPC.XPCSession) -> A) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946ad508  __TEXT,__text  implicit closure #3 (A) -> (XPC.XPCRichError) -> () in XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCReceivedMessage, A.Output == Swift.Encodable>((XPC.XPCSession) -> A) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946ad614  __TEXT,__text  XPC.XPCListener.IncomingSessionRequest._accept(cancellationHandler: (@Sendable (XPC.XPCRichError) -> ())?) -> (XPC.XPCListener.IncomingSessionRequest.Decision, XPC.XPCSession)
0x1946ad7cc  __TEXT,__text  _block_copy_helper.131
0x1946ad7d0  __TEXT,__text  XPC.XPCListener.IncomingSessionRequest.(decision in _FF1CDA90CF2FD1679E210A624A663AD3).setter : XPC.XPCListener.IncomingSessionRequest.Decision
0x1946ad8cc  __TEXT,__text  associated type witness table accessor for XPC._EncodingContainer.Container : XPC.EncodingGraph.Container in XPC._TopLevelEncoder : XPC._EncodingContainer in XPC
0x1946ad8d8  __TEXT,__text  generic specialization <XPC._TopLevelEncoder> of XPC._UnkeyedEncodingContainer._encodingContainer<A where A: XPC._EncodingContainer>(_: A.Type, forType: Any.Type?) -> A
0x1946ada78  __TEXT,__text  _block_copy_helper.223
0x1946ada7c  __TEXT,__text  generic specialization <Swift.CodingUserInfoKey, Any> of Swift._NativeDictionary.copy() -> ()
0x1946adc6c  __TEXT,__text  XPC.XPCSession.send<A, B where A: Swift.Encodable, B: Swift.Decodable>(_: A, replyHandler: (Swift.Result<B, Swift.Error>) -> ()) throws -> ()
0x1946adde4  __TEXT,__text  ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
0x1946ade40  __TEXT,__text  XPC._KeyedEncodingContainer.encode<A where A1: Swift.Encodable>(_: A1, forKey: A) throws -> ()
0x1946ae014  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode<A where A1: Swift.Encodable>(_: A1, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946ae050  __TEXT,__text  protocol witness for XPC._EncodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container?) -> A in conformance XPC._TopLevelEncoder : XPC._EncodingContainer in XPC
0x1946ae0d4  __TEXT,__text  protocol witness for XPC._EncodingContainer.container.getter : A.Container in conformance XPC._TopLevelEncoder : XPC._EncodingContainer in XPC
0x1946ae0dc  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.String, forKey: A) throws -> ()
0x1946ae1b8  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.String, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946ae1ec  __TEXT,__text  XPC._KeyedEncodingContainer.(_encode in _7E1E3A1581E9D210C0DAF0092A52A88E)(_: XPC.EncodingGraph.Value, forKey: A) -> ()
0x1946ae2d0  __TEXT,__text  XPC._KeyedGraphEncodingNode.__deallocating_deinit
0x1946ae304  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <Swift.ObjectIdentifier, Swift.UInt32> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x1946ae3ec  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.String) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946ae408  __TEXT,__text  XPC._TopLevelEncoder.singleValueContainer() -> Swift.SingleValueEncodingContainer
0x1946ae510  __TEXT,__text  lazy protocol witness table accessor for type XPC._SingleValueEncodingContainer and conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946ae564  __TEXT,__text  type metadata accessor for XPC.SingleValueGraphEncodingNode
0x1946ae588  __TEXT,__text  ___swift_exist.box.addr_destructor.5Tm
0x1946ae5e0  __TEXT,__text  ___swift_exist.box.addr_destructor.21
0x1946ae5fc  __TEXT,__text  merged function signature specialization <Arg[1] = Exploded> of XPC._SingleValueEncodingContainer.encode(Swift.Int) throws -> ()
0x1946ae720  __TEXT,__text  protocol witness for Swift.Encoder.singleValueContainer() -> Swift.SingleValueEncodingContainer in conformance XPC._TopLevelEncoder : Swift.Encoder in XPC
0x1946ae72c  __TEXT,__text  lazy protocol witness table accessor for type XPC._UnkeyedEncodingContainer and conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ae780  __TEXT,__text  type metadata accessor for XPC.UnkeyedGraphEncodingNode
0x1946ae7a4  __TEXT,__text  protocol witness for Swift.Encoder.unkeyedContainer() -> Swift.UnkeyedEncodingContainer in conformance XPC._TopLevelEncoder : Swift.Encoder in XPC
0x1946ae7b0  __TEXT,__text  XPC._TopLevelEncoder.unkeyedContainer() -> Swift.UnkeyedEncodingContainer
0x1946ae8b8  __TEXT,__text  lazy protocol witness table accessor for type XPC.IndexCodingKey and conformance XPC.IndexCodingKey : Swift.CodingKey in XPC
0x1946ae90c  __TEXT,__text  merged generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.String.Type) throws(Swift.DecodingError) -> Swift.String
0x1946aeaa4  __TEXT,__text  merged protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.String.Type) throws -> Swift.String in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946aebd8  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.String.Type) throws -> Swift.String in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946aec1c  __TEXT,__text  protocol witness for Swift.Decoder.singleValueContainer() throws -> Swift.SingleValueDecodingContainer in conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946aedc8  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.String.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.String
0x1946af148  __TEXT,__text  ___swift_exist.box.addr_destructorTm
0x1946af1a0  __TEXT,__text  ___swift_exist.box.addr_destructorTm
0x1946af1e4  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.String.Type, forKey: A) throws(Swift.DecodingError) -> Swift.String
0x1946af400  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.String.Type, forKey: A.Key) throws -> Swift.String in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946af504  __TEXT,__text  outlined init with copy of XPC.EncodingGraph.Value
0x1946af558  __TEXT,__text  XPC._SingleValueDecodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> XPC._SingleValueDecodingContainer
0x1946af780  __TEXT,__text  XPC._KeyedDecodingContainer.contains(A) -> Swift.Bool
0x1946af7ec  __TEXT,__text  protocol witness for XPC._DecodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> A in conformance XPC._KeyedDecodingContainer<A> : XPC._DecodingContainer in XPC
0x1946af90c  __TEXT,__text  XPC._TopLevelDecoder.(_container in _B16C06037F7910160B51B21A878A8EAE)<A where A: XPC._DecodingContainer>(A.Type) throws -> A
0x1946afa6c  __TEXT,__text  XPC.SerializedEncodingGraph.decode() throws -> XPC.EncodingGraph.Container
0x1946b11dc  __TEXT,__text  generic specialization <Swift.UInt32> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(A) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x1946b1218  __TEXT,__text  (extension in XPC):XPC.EncodingGraph.Container.tryDecodeAsXPCData<A where A1: Swift.Decodable>(_: A1.Type, at: [Swift.CodingKey]) throws(Swift.DecodingError) -> A1?
0x1946b18ec  __TEXT,__text  XPC._KeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> XPC._KeyedDecodingContainer<A>
0x1946b2028  __TEXT,__text  type metadata accessor for XPC._KeyedDecodingContainer
0x1946b2040  __TEXT,__text  partial apply forwarder for closure #1 (XPC.EncodingGraph.Key) -> A? in XPC._KeyedDecodingContainer.allKeys.getter : [A]
0x1946b205c  __TEXT,__text  generic specialization <XPC.EncodingGraph.Key, XPC.EncodingGraph.Value> of Swift._NativeDictionary._copyOrMoveAndResize(capacity: Swift.Int, moveElements: Swift.Bool) -> ()
0x1946b2338  __TEXT,__text  static XPC._KeyedDecodingContainer.(decodeDictionary in _75B0D857E5E60FECD69B41037A855175)(from: [XPC.EncodingGraph.Value], at: [Swift.CodingKey]) throws(Swift.DecodingError) -> [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value]
0x1946b2884  __TEXT,__text  XPC._KeyedDecodingContainer.(_container in _75B0D857E5E60FECD69B41037A855175)<A where A1: XPC._DecodingContainer>(_: A1.Type, forKey: XPC._KeyedEncodingContainer<A>._ContainerCodingKey, forType: Any.Type?) throws(Swift.DecodingError) -> A1
0x1946b2cc8  __TEXT,__text  XPC._KeyedDecodingContainer.(value in _75B0D857E5E60FECD69B41037A855175)(forKey: XPC._KeyedEncodingContainer<A>._ContainerCodingKey) throws(Swift.DecodingError) -> XPC.EncodingGraph.Value
0x1946b2ef0  __TEXT,__text  XPC._TopLevelDecoder.container<A where A: Swift.CodingKey>(keyedBy: A.Type) throws -> Swift.KeyedDecodingContainer<A>
0x1946b2f94  __TEXT,__text  protocol witness for Swift.Decoder.container<A where A1: Swift.CodingKey>(keyedBy: A1.Type) throws -> Swift.KeyedDecodingContainer<A1> in conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946b2fd0  __TEXT,__text  XPC.EncodingGraph.Value.unwrapIntoContainer() throws(XPC.EarlyDecodingError) -> XPC.EncodingGraph.Container
0x1946b3188  __TEXT,__text  XPC._TopLevelDecoder.decode<A where A: Swift.Decodable>(A.Type) throws -> A
0x1946b3488  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode<A where A1: Swift.Decodable>(_: A1.Type, forKey: A.Key) throws -> A1 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b34c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> () with unmangled suffix ".11"
0x1946b34c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> () with unmangled suffix ".11"
0x1946b34c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> () with unmangled suffix ".11"
0x1946b34c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> () with unmangled suffix ".11"
0x1946b34c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> () with unmangled suffix ".11"
0x1946b34c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> () with unmangled suffix ".11"
0x1946b34c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> () with unmangled suffix ".11"
0x1946b34c4  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCDictionary) -> XPC.XPCDictionary?) -> () with unmangled suffix ".11"
0x1946b34c8  __TEXT,__text  partial apply forwarder for closure #1 (XPC.XPCDictionary) -> XPC.XPCDictionary? in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCReceivedMessage) -> Swift.Encodable?) -> ()
0x1946b34d0  __TEXT,__text  partial apply forwarder for closure #1 (XPC.XPCDictionary) -> XPC.XPCDictionary? in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCReceivedMessage) -> Swift.Encodable?) -> () with unmangled suffix ".43"
0x1946b34d4  __TEXT,__text  implicit closure #2 (XPC.XPCReceivedMessage) -> Swift.Encodable? in implicit closure #1 (XPC.ClientSpecifiedHandler<XPC.XPCReceivedMessage, Swift.Encodable?>) -> (XPC.XPCReceivedMessage) -> Swift.Encodable? in XPC.XPCSession.setIncomingMessageHandler((XPC.XPCReceivedMessage) -> Swift.Encodable?) -> 
0x1946b3548  __TEXT,__text  partial apply forwarder for implicit closure #2 (XPC.XPCReceivedMessage) -> Swift.Encodable? in implicit closure #1 (XPC.ClientSpecifiedHandler<XPC.XPCReceivedMessage, Swift.Encodable?>) -> (XPC.XPCReceivedMessage) -> Swift.Encodable? in XPC.XPCSession.setIncomingMessageHandler((XPC.XPCReceivedMessa
0x1946b35e8  __TEXT,__text  closure #1 (XPC.XPCDictionary) -> XPC.XPCDictionary? in XPC.XPCSession._setIncomingMessageHandler((XPC.XPCReceivedMessage) -> Swift.Encodable?) -> ()
0x1946b37d8  __TEXT,__text  generic specialization <Swift.UInt32, XPC.DecodedContainer> of Swift._NativeDictionary._copyOrMoveAndResize(capacity: Swift.Int, moveElements: Swift.Bool) -> ()
0x1946b3a28  __TEXT,__text  outlined init with copy of [Swift.CodingUserInfoKey : Any]
0x1946b3a90  __TEXT,__text  XPC._KeyedDecodingContainer.nestedContainer<A where A1: Swift.CodingKey>(keyedBy: A1.Type, forKey: A) throws(Swift.DecodingError) -> Swift.KeyedDecodingContainer<A1>
0x1946b3ce4  __TEXT,__text  XPC._KeyedDecodingContainer.allKeys.getter : [A]
0x1946b3d84  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.allKeys.getter : [A.Key] in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b3d90  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.nestedContainer<A where A1: Swift.CodingKey>(keyedBy: A1.Type, forKey: A.Key) throws -> Swift.KeyedDecodingContainer<A1> in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b3ebc  __TEXT,__text  outlined destroy of Swift.Encodable?
0x1946b3f1c  __TEXT,__text  (extension in XPC):XPC.EncodingGraph.Container.(maybeFoundationData in _B60F660E558EB6466291C850CECEFCD0).getter : XPC.XPCData?
0x1946b4078  __TEXT,__text  type metadata accessor for XPC.XPCReceivedMessage.XPCReceivedMessageMetadata
0x1946b410c  __TEXT,__text  generic specialization <Swift.Int64> of XPC.XPCDictionary.subscript.getter : <A where A: Swift.BinaryInteger>(_: Swift.String, as: A.Type) -> A?
0x1946b420c  __TEXT,__text  function signature specialization <Arg[1] = Dead> of XPC.XPCDictionary.subscript.getter : (_: Swift.String, as: __C.OS_xpc_object.Type) -> __C.OS_xpc_object?
0x1946b4280  __TEXT,__text  partial apply forwarder for implicit closure #2 (XPC.XPCReceivedMessage) -> Swift.Encodable? in implicit closure #1 (A) -> (XPC.XPCReceivedMessage) -> Swift.Encodable? in XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCReceivedMessage, A.Output == Swift
0x1946b43e0  __TEXT,__text  type metadata accessor for XPC.DecodedContainer
0x1946b4404  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <Swift.UInt32, XPC.DecodedContainer> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x1946b4514  __TEXT,__text  function signature specialization <Arg[1] = Dead> of XPC.SerializedEncodingGraph.Tag.init(rawValue: Swift.UInt8) -> XPC.SerializedEncodingGraph.Tag?
0x1946b4520  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.UInt64) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946b4540  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent<A where A1: Swift.Encodable>(_: A1?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946b456c  __TEXT,__text  merged XPC._KeyedEncodingContainer.nestedUnkeyedContainer(forKey: A) -> Swift.UnkeyedEncodingContainer
0x1946b4704  __TEXT,__text  merged protocol witness for Swift.KeyedEncodingContainerProtocol.nestedUnkeyedContainer(forKey: A.Key) -> Swift.UnkeyedEncodingContainer in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946b474c  __TEXT,__text  protocol witness for XPC._EncodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container?) -> A in conformance XPC._UnkeyedEncodingContainer : XPC._EncodingContainer in XPC
0x1946b47d4  __TEXT,__text  merged function signature specialization <Arg[1] = Exploded> of XPC._SingleValueEncodingContainer.encode(Swift.Int32) throws -> ()
0x1946b48fc  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.UInt8>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946b4924  __TEXT,__text  closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> Swift.Bool in XPC._UnkeyedEncodingContainer.encode<A where A: Swift.Sequence, A.Element == Swift.UInt8>(contentsOf: A) throws -> ()
0x1946b4ab4  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.nestedUnkeyedContainer(forKey: A.Key) -> Swift.UnkeyedEncodingContainer in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946b4ae4  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.UInt32) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946b4b04  __TEXT,__text  XPC._UnkeyedEncodingContainer.encode<A where A: Swift.Sequence, A.Element == Swift.UInt8>(contentsOf: A) throws -> ()
0x1946b4df4  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> Swift.Bool in XPC._UnkeyedEncodingContainer.encode<A where A: Swift.Sequence, A.Element == Swift.UInt8>(contentsOf: A) throws -> ()
0x1946b4e14  __TEXT,__text  ___swift_exist.box.addr_destructor.12
0x1946b4f5c  __TEXT,__text  function signature specialization <Arg[1] = Exploded> of XPC._SingleValueEncodingContainer.encode(Swift.String) throws -> ()
0x1946b50a8  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Encodable>(A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946b50d0  __TEXT,__text  protocol witness for XPC.EncodingGraph.Container.values.getter : [XPC.EncodingGraph.Value] in conformance XPC.SingleValueGraphEncodingNode : XPC.EncodingGraph.Container in XPC
0x1946b50d0  __TEXT,__text  protocol witness for XPC.EncodingGraph.Container.values.getter : [XPC.EncodingGraph.Value] in conformance XPC.SingleValueGraphEncodingNode : XPC.EncodingGraph.Container in XPC
0x1946b5108  __TEXT,__text  ___swift_exist.box.addr_destructor.24
0x1946b510c  __TEXT,__text  XPC._UnkeyedEncodingContainer.encode<A where A: Swift.Encodable>(A) throws -> ()
0x1946b51e8  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.UInt8) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946b5208  __TEXT,__text  merged function signature specialization <Arg[1] = Exploded> of XPC._SingleValueEncodingContainer.encode(Swift.Int8) throws -> ()
0x1946b5330  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.Double) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946b534c  __TEXT,__text  function signature specialization <Arg[1] = Exploded> of XPC._SingleValueEncodingContainer.encode(Swift.Double) throws -> ()
0x1946b5470  __TEXT,__text  merged protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Double.Type) throws -> Swift.Double in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946b55a4  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Double.Type) throws -> Swift.Double in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946b55e8  __TEXT,__text  merged generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Double.Type) throws(Swift.DecodingError) -> Swift.Double
0x1946b5788  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.Double.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.Double
0x1946b5afc  __TEXT,__text  outlined init with take of XPC.XPCCodableObjectRepresentable
0x1946b5afc  __TEXT,__text  outlined init with take of XPC.XPCCodableObjectRepresentable
0x1946b5b14  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.Bool) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946b5b30  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.contains(A.Key) -> Swift.Bool in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b5b3c  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent<A where A1: Swift.Decodable>(_: A1.Type, forKey: A.Key) throws -> A1? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b5b68  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.String.Type, forKey: A.Key) throws -> Swift.String? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b5c54  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed () -> () to @escaping @callee_unowned @convention(block) () -> ()
0x1946b5f34  __TEXT,__text  type metadata instantiation function for XPC._KeyedDecodingContainer
0x1946b5f70  __TEXT,__text  function signature specialization <Arg[1] = Existential To Protocol Constrained Generic> of XPC._TopLevelDecoder.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) -> XPC._TopLevelDecoder
0x1946b5f80  __TEXT,__text  lazy protocol witness table accessor for type XPC._TopLevelDecoder and conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946b5fd4  __TEXT,__text  generic specialization <Swift.UInt32> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(_: A, hashValue: Swift.Int) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x1946b6040  __TEXT,__text  protocol witness for XPC.EncodingGraph.Container.values.getter : [XPC.EncodingGraph.Value] in conformance XPC.DecodedContainer : XPC.EncodingGraph.Container in XPC
0x1946b6050  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <XPC.EncodingGraph.Key, XPC.EncodingGraph.Value> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x1946b6188  __TEXT,__text  generic specialization <Swift.UInt32, XPC.DecodedContainer> of Swift._NativeDictionary._delete(at: Swift._HashTable.Bucket) -> ()
0x1946b62fc  __TEXT,__text  protocol witness for XPC._DecodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> A in conformance XPC._TopLevelDecoder : XPC._DecodingContainer in XPC
0x1946b630c  __TEXT,__text  ___swift_exist.box.addr_destructor.6
0x1946b6328  __TEXT,__text  XPC._KeyedDecodingContainer.(value in _75B0D857E5E60FECD69B41037A855175)(forKey: A) throws(Swift.DecodingError) -> XPC.EncodingGraph.Value
0x1946b6528  __TEXT,__text  outlined init with copy of XPC._SingleValueDecodingContainer
0x1946b6560  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.EncodingGraph.Key
0x1946b65ac  __TEXT,__text  closure #1 (XPC.EncodingGraph.Key) -> A? in XPC._KeyedDecodingContainer.allKeys.getter : [A]
0x1946b664c  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.EncodingGraph.Key
0x1946b66a0  __TEXT,__text  ___swift_memcpy16_8
0x1946b66ac  __TEXT,__text  lazy protocol witness table accessor for type [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value].Keys and conformance [A : B].Keys : Swift.Sequence in Swift
0x1946b6710  __TEXT,__text  lazy protocol witness table accessor for type XPC._SingleValueDecodingContainer and conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946b6764  __TEXT,__text  base witness table accessor for Swift.CustomDebugStringConvertible in XPC.IndexCodingKey : Swift.CodingKey in XPC
0x1946b6768  __TEXT,__text  lazy protocol witness table accessor for type XPC.IndexCodingKey and conformance XPC.IndexCodingKey : Swift.CustomDebugStringConvertible in XPC
0x1946b67bc  __TEXT,__text  lazy protocol witness table accessor for type XPC.IndexCodingKey and conformance XPC.IndexCodingKey : Swift.CustomStringConvertible in XPC
0x1946b6810  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.Int) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946b6830  __TEXT,__text  merged XPC.XPCDictionary.subscript.setter : <A where A: Swift.SignedInteger>(Swift.String) -> A?
0x1946b68c8  __TEXT,__text  merged function signature specialization <Arg[0] = Owned To Guaranteed> of XPC.XPCDictionary.subscript.setter : <A where A: Swift.SignedInteger>(Swift.String) -> A?
0x1946b6988  __TEXT,__text  Swift.Optional.flatMap<A, B where A1: Swift.Error, B1: ~Swift.Copyable>((A) throws(A1) -> B1?) throws(A1) -> B1?
0x1946b6aec  __TEXT,__text  partial apply forwarder for implicit closure #1 (A) -> Swift.UInt64? in XPC.XPCDictionary.subscript.setter : <A where A: Swift.UnsignedInteger>(Swift.String) -> A?
0x1946b6b0c  __TEXT,__text  implicit closure #1 (A) -> Swift.UInt64? in XPC.XPCDictionary.subscript.setter : <A where A: Swift.UnsignedInteger>(Swift.String) -> A?
0x1946b7060  __TEXT,__text  base witness table accessor for Swift.CustomStringConvertible in XPC.IndexCodingKey : Swift.CodingKey in XPC
0x1946b7064  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.Int16) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946b7084  __TEXT,__text  merged function signature specialization <Arg[1] = Exploded> of XPC._SingleValueEncodingContainer.encode(Swift.Int16) throws -> ()
0x1946b71ac  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.String?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946b71c4  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.Int, forKey: A) throws -> ()
0x1946b7208  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946b7234  __TEXT,__text  merged protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946b72a0  __TEXT,__text  lazy protocol witness table accessor for type Swift.UInt64 and conformance Swift.UInt64 : Swift.BinaryInteger in Swift
0x1946b762c  __TEXT,__text  ___swift_exist.box.addr_destructor.3
0x1946b7648  __TEXT,__text  XPC._SingleValueEncodingContainer.encode<A where A: Swift.Encodable>(A) throws -> ()
0x1946b7858  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode<A where A1: Swift.Encodable>(A1) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946b7880  __TEXT,__text  XPC._SingleValueDecodingContainer.decode<A where A: Swift.Decodable>(A.Type) throws -> A
0x1946b7ae0  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode<A where A1: Swift.Decodable>(A1.Type) throws -> A1 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946b7af8  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode<A where A: Swift.Decodable>(A.Type) throws -> A
0x1946b7cac  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt64.Type) throws -> Swift.UInt64 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946b7cd8  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.UInt64.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.UInt64
0x1946b8044  __TEXT,__text  merged protocol witness for Swift.KeyedDecodingContainerProtocol.decodeNil(forKey: A.Key) throws -> Swift.Bool in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b8154  __TEXT,__text  XPC._KeyedDecodingContainer.decodeNil(forKey: A) throws(Swift.DecodingError) -> Swift.Bool
0x1946b8308  __TEXT,__text  function signature specialization <Arg[0] = Existential To Protocol Constrained Generic> of XPC.EncodingGraph.Value.decodeNil(for: XPC._DecodingContainer) -> Swift.Bool
0x1946b84bc  __TEXT,__text  XPC.SingleValueDecodingContainer4OptionalPrimitive.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> XPC.SingleValueDecodingContainer4OptionalPrimitive
0x1946b8810  __TEXT,__text  protocol witness for XPC._DecodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC._TopLevelDecoder : XPC._DecodingContainer in XPC
0x1946b8810  __TEXT,__text  protocol witness for XPC._DecodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC._TopLevelDecoder : XPC._DecodingContainer in XPC
0x1946b8810  __TEXT,__text  protocol witness for XPC._DecodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC._TopLevelDecoder : XPC._DecodingContainer in XPC
0x1946b8810  __TEXT,__text  protocol witness for XPC._DecodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC._TopLevelDecoder : XPC._DecodingContainer in XPC
0x1946b8810  __TEXT,__text  protocol witness for XPC._DecodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC._TopLevelDecoder : XPC._DecodingContainer in XPC
0x1946b8810  __TEXT,__text  protocol witness for XPC._DecodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC._TopLevelDecoder : XPC._DecodingContainer in XPC
0x1946b8810  __TEXT,__text  protocol witness for XPC._DecodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC._TopLevelDecoder : XPC._DecodingContainer in XPC
0x1946b8858  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.nestedUnkeyedContainer(forKey: A.Key) throws -> Swift.UnkeyedDecodingContainer in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b8884  __TEXT,__text  merged protocol witness for Swift.KeyedDecodingContainerProtocol.nestedUnkeyedContainer(forKey: A.Key) throws -> Swift.UnkeyedDecodingContainer in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b89a0  __TEXT,__text  XPC._KeyedDecodingContainer.nestedUnkeyedContainer(forKey: A) throws(Swift.DecodingError) -> Swift.UnkeyedDecodingContainer
0x1946b8bd4  __TEXT,__text  protocol witness for XPC._DecodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> A in conformance XPC._UnkeyedDecodingContainer : XPC._DecodingContainer in XPC
0x1946b8cf8  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt32.Type) throws -> Swift.UInt32 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946b8d38  __TEXT,__text  merged protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int32.Type) throws -> Swift.Int32 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946b8e54  __TEXT,__text  merged generic specialization <XPC._SingleValueDecodingContainer> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt32.Type) throws(Swift.DecodingError) -> Swift.UInt32
0x1946b8fe4  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.UInt32.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.UInt32
0x1946b9350  __TEXT,__text  type metadata accessor for XPC.EncodingGraph.ContainerMetadata
0x1946b9360  __TEXT,__text  XPC._KeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, dictionary: [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value]) -> XPC._KeyedDecodingContainer<A>
0x1946b9360  __TEXT,__text  XPC._KeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, dictionary: [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value]) -> XPC._KeyedDecodingContainer<A>
0x1946b9360  __TEXT,__text  XPC._KeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, dictionary: [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value]) -> XPC._KeyedDecodingContainer<A>
0x1946b9360  __TEXT,__text  XPC._KeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, dictionary: [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value]) -> XPC._KeyedDecodingContainer<A>
0x1946b9360  __TEXT,__text  XPC._KeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, dictionary: [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value]) -> XPC._KeyedDecodingContainer<A>
0x1946b9360  __TEXT,__text  XPC._KeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, dictionary: [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value]) -> XPC._KeyedDecodingContainer<A>
0x1946b9360  __TEXT,__text  XPC._KeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, dictionary: [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value]) -> XPC._KeyedDecodingContainer<A>
0x1946b9360  __TEXT,__text  XPC._KeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, dictionary: [XPC.EncodingGraph.Key : XPC.EncodingGraph.Value]) -> XPC._KeyedDecodingContainer<A>
0x1946b9364  __TEXT,__text  merged protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int.Type) throws -> Swift.Int in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946b9470  __TEXT,__text  generic specialization <XPC._SingleValueDecodingContainer> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt64.Type) throws(Swift.DecodingError) -> Swift.UInt64
0x1946b95f0  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeNil(forKey: A.Key) throws -> Swift.Bool in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946b9620  __TEXT,__text  lazy protocol witness table accessor for type XPC._UnkeyedDecodingContainer and conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946b9674  __TEXT,__text  XPC._UnkeyedDecodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> XPC._UnkeyedDecodingContainer
0x1946b9ca4  __TEXT,__text  ___swift_memcpy1_1
0x1946b9cb0  __TEXT,__text  getEnumTag value witness for XPC.EncodingGraph.ContainerMetadata
0x1946b9cb0  __TEXT,__text  getEnumTag value witness for XPC.EncodingGraph.ContainerMetadata
0x1946b9cb8  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode<A where A1: Swift.Decodable>(A1.Type) throws -> A1 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946b9cd0  __TEXT,__text  generic specialization <XPC._TopLevelDecoder> of XPC._UnkeyedDecodingContainer.(_container in _1016890FE93F2D24F6CF826DE25716D5)<A where A: XPC._DecodingContainer>(_: A.Type, forType: Any.Type?) throws(Swift.DecodingError) -> A
0x1946b9f88  __TEXT,__text  XPC._UnkeyedDecodingContainer.(_decodeNext in _1016890FE93F2D24F6CF826DE25716D5)() throws(Swift.DecodingError) -> XPC.EncodingGraph.Value
0x1946ba160  __TEXT,__text  merged protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int8.Type) throws -> Swift.Int8 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946ba27c  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt8.Type) throws -> Swift.UInt8 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946ba2bc  __TEXT,__text  protocol witness for Swift.Decoder.unkeyedContainer() throws -> Swift.UnkeyedDecodingContainer in conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946ba478  __TEXT,__text  merged closure #1 (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> () in XPC.XPCSession._send<A where A: Swift.Encodable>(_: A, replyHandler: (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> ()) throws -> ()
0x1946ba5a8  __TEXT,__text  partial apply forwarder for implicit closure #2 (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> () in implicit closure #1 (XPC.ClientSpecifiedHandler<Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>, ()>) -> (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> () in XPC.XPCS
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ()) with unmangled suffix ".7"
0x1946ba5d8  __TEXT,__text  outlined consume of Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>
0x1946ba618  __TEXT,__text  _block_destroy_helper.224
0x1946ba61c  __TEXT,__text  ___swift_closure_destructor.217
0x1946ba620  __TEXT,__text  ___swift_closure_destructor.84
0x1946ba624  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object?, __C.OS_xpc_object?) -> () in XPC.XPCSession._send(message: XPC.XPCDictionary, replyHandler: (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> ()) -> () with unmangled suffix ".202"
0x1946ba624  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object?, __C.OS_xpc_object?) -> () in XPC.XPCSession._send(message: XPC.XPCDictionary, replyHandler: (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> ()) -> () with unmangled suffix ".202"
0x1946ba628  __TEXT,__text  partial apply forwarder for closure #1 (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> () in XPC.XPCSession.send<A where A: Swift.Encodable>(_: A, userInfo: [Swift.CodingUserInfoKey : Any], replyHandler: @Sendable (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> ()) throws -> ()
0x1946ba644  __TEXT,__text  partial apply forwarder for closure #1 (Swift.Result<XPC.XPCDictionary, XPC.XPCRichError>) -> () in XPC.XPCSession._send<A where A: Swift.Encodable>(_: A, replyHandler: (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> ()) throws -> ()
0x1946ba648  __TEXT,__text  ___swift_exist.box.addr_destructor.2
0x1946ba650  __TEXT,__text  ___swift_exist.box.addr_destructor.2
0x1946ba654  __TEXT,__text  ___swift_exist.box.addr_destructor.2
0x1946ba65c  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.isAtEnd.getter : Swift.Bool in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946ba680  __TEXT,__text  ___swift_closure_destructor.220
0x1946ba684  __TEXT,__text  ___swift_closure_destructor.81
0x1946ba688  __TEXT,__text  protocol witness for Swift.Decoder.codingPath.getter : [Swift.CodingKey] in conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946ba688  __TEXT,__text  protocol witness for Swift.Decoder.codingPath.getter : [Swift.CodingKey] in conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946ba688  __TEXT,__text  protocol witness for Swift.Decoder.codingPath.getter : [Swift.CodingKey] in conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946ba688  __TEXT,__text  protocol witness for Swift.Decoder.codingPath.getter : [Swift.CodingKey] in conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946ba690  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.UInt8.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.UInt8
0x1946ba9fc  __TEXT,__text  ___swift_project_boxed_opaque_existential_1
0x1946baa2c  __TEXT,__text  function signature specialization <Arg[1] = Exploded> of XPC._SingleValueEncodingContainer.encode(Swift.Bool) throws -> ()
0x1946bab48  __TEXT,__text  merged protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Bool.Type) throws -> Swift.Bool in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946bac80  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Bool.Type) throws -> Swift.Bool in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946bacc8  __TEXT,__text  merged generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Bool.Type) throws(Swift.DecodingError) -> Swift.Bool
0x1946bae58  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.Bool.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.Bool
0x1946bb1c0  __TEXT,__text  merged generic specialization <XPC._SingleValueDecodingContainer> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt8.Type) throws(Swift.DecodingError) -> Swift.UInt8
0x1946bb4ec  __TEXT,__text  __swift_xpc_peer_requirement_create_entitlement_exists
0x1946bb550  __TEXT,__text  __swift__xpc_peer_requirement_match_token
0x1946bb5a0  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int.Type) throws -> Swift.Int in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946bb5cc  __TEXT,__text  generic specialization <XPC._SingleValueDecodingContainer> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int.Type) throws(Swift.DecodingError) -> Swift.Int
0x1946bb74c  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.Int.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.Int
0x1946bbab8  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int16.Type) throws -> Swift.Int16 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946bbaf8  __TEXT,__text  merged protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int16.Type) throws -> Swift.Int16 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946bbc14  __TEXT,__text  merged generic specialization <XPC._SingleValueDecodingContainer> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt16.Type) throws(Swift.DecodingError) -> Swift.UInt16
0x1946bbda4  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.Int16.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.Int16
0x1946bc110  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int.Type, forKey: A.Key) throws -> Swift.Int in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bc13c  __TEXT,__text  merged protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int.Type, forKey: A.Key) throws -> Swift.Int in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bc24c  __TEXT,__text  merged XPC._KeyedDecodingContainer.decode(_: Swift.Int.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Int
0x1946bc470  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.Bool, forKey: A) throws -> ()
0x1946bc4b4  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Bool, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bc4dc  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.Double, forKey: A) throws -> ()
0x1946bc53c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Double, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bc564  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.Int32?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bc580  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Bool.Type, forKey: A.Key) throws -> Swift.Bool in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bc5b0  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.Bool.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Bool
0x1946bc7c4  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Double.Type, forKey: A.Key) throws -> Swift.Double in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bc8c8  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.Double.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Double
0x1946bcae4  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Int32.Type, forKey: A.Key) throws -> Swift.Int32? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bcb00  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.String.Type) throws(Swift.DecodingError) -> Swift.String
0x1946bcb44  __TEXT,__text  protocol witness for XPC._DecodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : XPC._DecodingContainer in XPC
0x1946bcb44  __TEXT,__text  protocol witness for XPC._DecodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : XPC._DecodingContainer in XPC
0x1946bcb4c  __TEXT,__text  outlined init with copy of XPC.SingleValueDecodingContainer4OptionalPrimitive
0x1946bcb84  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Int64.Type, forKey: A.Key) throws -> Swift.Int64? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bcb9c  __TEXT,__text  (extension in XPC):XPC._DecodingContainer.codingPath.getter : [Swift.CodingKey]
0x1946bcbdc  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.codingPath.getter : [Swift.CodingKey] in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bcbe8  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.count.getter : Swift.Int? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946bcc04  __TEXT,__text  XPC.XPCSession.cancel(reason: Swift.String) -> ()
0x1946bcc28  __TEXT,__text  __swift_xpc_session_cancel
0x1946bcc84  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> ()
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc8c  __TEXT,__text  partial apply forwarder for closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> () with unmangled suffix ".11"
0x1946bcc90  __TEXT,__text  closure #1 (__C.OS_xpc_object) -> () in XPC.XPCSession.setCancellationHandler((XPC.XPCRichError) -> ()) -> ()
0x1946bcd50  __TEXT,__text  ___swift_memcpy24_8
0x1946bcd64  __TEXT,__text  protocol witness for Swift.CustomDebugStringConvertible.debugDescription.getter : Swift.String in conformance XPC.XPCRichError : Swift.CustomDebugStringConvertible in XPC
0x1946bcd94  __TEXT,__text  _block_destroy_helper.49
0x1946bcd98  __TEXT,__text  ___swift_closure_destructor.45
0x1946bcd9c  __TEXT,__text  ___swift_closure_destructor.41
0x1946bcda0  __TEXT,__text  ___swift_closure_destructor.38
0x1946bcda4  __TEXT,__text  _block_destroy_helper.172
0x1946bcda8  __TEXT,__text  ___swift_closure_destructor.168
0x1946bcdac  __TEXT,__text  ___swift_closure_destructor.164
0x1946bcdb0  __TEXT,__text  protocol witness for Swift.Decoder.userInfo.getter : [Swift.CodingUserInfoKey : Any] in conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946bcdb0  __TEXT,__text  protocol witness for Swift.Decoder.userInfo.getter : [Swift.CodingUserInfoKey : Any] in conformance XPC._TopLevelDecoder : Swift.Decoder in XPC
0x1946bcdb8  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.UInt32.Type, forKey: A.Key) throws -> Swift.UInt32 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bcde4  __TEXT,__text  merged protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int32.Type, forKey: A.Key) throws -> Swift.Int32 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bcef4  __TEXT,__text  merged XPC._KeyedDecodingContainer.decode(_: Swift.Int32.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Int32
0x1946bd118  __TEXT,__text  protocol witness for Swift.Decodable.init(from: Swift.Decoder) throws -> A in conformance XPC.XPCCodableObject : Swift.Decodable in XPC
0x1946bd130  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Bool) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946bd624  __TEXT,__text  merged XPC._KeyedEncodingContainer.encode(_: Swift.Int32, forKey: A) throws -> ()
0x1946bd66c  __TEXT,__text  merged protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int32, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bd6a4  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.UInt32, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bd6c0  __TEXT,__text  protocol witness for Swift.Encodable.encode(to: Swift.Encoder) throws -> () in conformance XPC.XPCCodableObject : Swift.Encodable in XPC
0x1946bd9e8  __TEXT,__text  protocol witness for Swift.Encoder.userInfo.getter : [Swift.CodingUserInfoKey : Any] in conformance XPC._TopLevelEncoder : Swift.Encoder in XPC
0x1946bd9f0  __TEXT,__text  ___swift_mutable_project_boxed_opaque_existential_1
0x1946bda2c  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.UInt64) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946bda48  __TEXT,__text  merged protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946bdb4c  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.UInt64.Type) throws -> Swift.UInt64 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946bdb78  __TEXT,__text  merged XPC._UnkeyedDecodingContainer.decode(Swift.Int.Type) throws(Swift.DecodingError) -> Swift.Int
0x1946bde74  __TEXT,__text  merged protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int.Type) throws -> Swift.Int in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946bdf60  __TEXT,__text  outlined init with copy of XPC._UnkeyedDecodingContainer
0x1946bdf98  __TEXT,__text  XPC._UnkeyedDecodingContainer.decodeNil() throws -> Swift.Bool
0x1946be304  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeNil() throws -> Swift.Bool in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946be320  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent<A where A1: Swift.Decodable>(A1.Type) throws -> A1? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946be34c  __TEXT,__text  closure #1 (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> () in XPC.XPCSession.send<A, B where A: Swift.Encodable, B: Swift.Decodable>(_: A, replyHandler: (Swift.Result<B, Swift.Error>) -> ()) throws -> ()
0x1946be488  __TEXT,__text  partial apply forwarder for closure #1 (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> () in XPC.XPCSession.send<A, B where A: Swift.Encodable, B: Swift.Decodable>(_: A, replyHandler: (Swift.Result<B, Swift.Error>) -> ()) throws -> ()
0x1946be498  __TEXT,__text  closure #1 () -> Swift.Result<B, Swift.Error> in closure #1 (Swift.Result<XPC.XPCReceivedMessage, XPC.XPCRichError>) -> () in XPC.XPCSession.send<A, B where A: Swift.Encodable, B: Swift.Decodable>(_: A, replyHandler: (Swift.Result<B, Swift.Error>) -> ()) throws -> ()
0x1946be694  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Bool.Type) throws -> Swift.Bool in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946be77c  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.Bool.Type) throws(Swift.DecodingError) -> Swift.Bool
0x1946bea6c  __TEXT,__text  partial apply forwarder for reabstraction thunk helper <A, B where A: Swift.Encodable, B: Swift.Decodable> from @escaping @callee_guaranteed (@in_guaranteed Swift.Result<B, Swift.Error>) -> () to @escaping @callee_guaranteed (@in_guaranteed Swift.Result<B, Swift.Error>) -> (@out ())
0x1946bea94  __TEXT,__text  ___swift_closure_destructor.78
0x1946bea98  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance XPC.XPCArray : Swift.Equatable in XPC
0x1946bea98  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance XPC.XPCArray : Swift.Equatable in XPC
0x1946bea98  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance XPC.XPCArray : Swift.Equatable in XPC
0x1946bea98  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance XPC.XPCArray : Swift.Equatable in XPC
0x1946beac4  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int32, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946beaec  __TEXT,__text  __swift_xpc_listener_create
0x1946bee44  __TEXT,__text  _block_copy_helper.12
0x1946bee48  __TEXT,__text  _block_copy_helper.12
0x1946bee4c  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int32.Type, forKey: A.Key) throws -> Swift.Int32 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bee78  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.Int32.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.Int32
0x1946bf1ec  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.Float?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bf208  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.Float, forKey: A) throws -> ()
0x1946bf26c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Float, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bf294  __TEXT,__text  static Swift.String._copying(Swift.String) -> Swift.String
0x1946bf314  __TEXT,__text  static Swift.String._copying(Swift.Substring) -> Swift.String
0x1946bf45c  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Float.Type, forKey: A.Key) throws -> Swift.Float? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bf478  __TEXT,__text  generic specialization <serialized, Swift.Substring.UTF8View> of (extension in Swift):Swift.Sequence._copySequenceContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int)
0x1946bf674  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.Int64?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bf68c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int64, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bf6b8  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.UInt64.Type, forKey: A.Key) throws -> Swift.UInt64 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bf6e4  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.Int64, forKey: A) throws -> ()
0x1946bf728  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Bool.Type, forKey: A.Key) throws -> Swift.Bool? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bf740  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Int.Type, forKey: A.Key) throws -> Swift.Int? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bf758  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int.Type) throws(Swift.DecodingError) -> Swift.Int
0x1946bf8d8  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.UInt, forKey: A) throws -> ()
0x1946bf91c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.UInt, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bf948  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Float.Type, forKey: A.Key) throws -> Swift.Float in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946bfa4c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.Bool?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946bfa64  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.Float.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Float
0x1946bfc80  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.Float.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.Float
0x1946bfff4  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.UInt64, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946c0020  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int64.Type, forKey: A.Key) throws -> Swift.Int64 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c004c  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.Int64.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.Int64
0x1946c03b8  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.UInt64, forKey: A) throws -> ()
0x1946c0454  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encodeNil() throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946c0470  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946c048c  __TEXT,__text  XPC._UnkeyedEncodingContainer.nestedContainer<A where A: Swift.CodingKey>(keyedBy: A.Type) -> Swift.KeyedEncodingContainer<A>
0x1946c0558  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.nestedContainer<A where A1: Swift.CodingKey>(keyedBy: A1.Type) -> Swift.KeyedEncodingContainer<A1> in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946c056c  __TEXT,__text  XPC._UnkeyedEncodingContainer._encodingContainer<A where A: XPC._EncodingContainer>(_: A.Type, forType: Any.Type?) -> A
0x1946c0784  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.UInt.Type, forKey: A.Key) throws -> Swift.UInt in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c07b0  __TEXT,__text  XPC.EncodingGraph.Value.decode(as: Swift.UInt.Type, for: XPC._DecodingContainer) throws(Swift.DecodingError) -> Swift.UInt
0x1946c0b1c  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decodeNil() -> Swift.Bool in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c0b1c  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decodeNil() -> Swift.Bool in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c0b44  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.nestedContainer<A where A1: Swift.CodingKey>(keyedBy: A1.Type) throws -> Swift.KeyedDecodingContainer<A1> in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c0b5c  __TEXT,__text  XPC._UnkeyedDecodingContainer.nestedContainer<A where A: Swift.CodingKey>(keyedBy: A.Type) throws -> Swift.KeyedDecodingContainer<A>
0x1946c0cc4  __TEXT,__text  XPC._UnkeyedDecodingContainer.(_container in _1016890FE93F2D24F6CF826DE25716D5)<A where A: XPC._DecodingContainer>(_: A.Type, forType: Any.Type?) throws(Swift.DecodingError) -> A
0x1946c1008  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int.Type) throws -> Swift.Int in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c1034  __TEXT,__text  _block_copy_helper.43
0x1946c1038  __TEXT,__text  protocol witness for Swift.Error._domain.getter : Swift.String in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946c1038  __TEXT,__text  protocol witness for Swift.Error._domain.getter : Swift.String in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946c1038  __TEXT,__text  protocol witness for Swift.Error._domain.getter : Swift.String in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946c103c  __TEXT,__text  protocol witness for Swift.Error._code.getter : Swift.Int in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946c103c  __TEXT,__text  protocol witness for Swift.Error._code.getter : Swift.Int in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946c103c  __TEXT,__text  protocol witness for Swift.Error._code.getter : Swift.Int in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946c1040  __TEXT,__text  protocol witness for Swift.Error._userInfo.getter : Swift.AnyObject? in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946c1040  __TEXT,__text  protocol witness for Swift.Error._userInfo.getter : Swift.AnyObject? in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946c1040  __TEXT,__text  protocol witness for Swift.Error._userInfo.getter : Swift.AnyObject? in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946c1044  __TEXT,__text  partial apply forwarder for implicit closure #4 (XPC.XPCRichError) -> () in implicit closure #3 (A) -> (XPC.XPCRichError) -> () in XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCReceivedMessage, A.Output == Swift.Encodable>((XPC.XPCSession) -> A) -> XP
0x1946c1048  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> () to @escaping @callee_guaranteed (@in_guaranteed XPC.XPCRichError) -> (@out ())
0x1946c1070  __TEXT,__text  partial apply forwarder for implicit closure #4 (XPC.XPCRichError) -> () in implicit closure #3 (A) -> (XPC.XPCRichError) -> () in XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCDictionary, A.Output == XPC.XPCDictionary>((XPC.XPCSession) -> A) -> XPC.X
0x1946c1074  __TEXT,__text  merged partial apply forwarder for implicit closure #4 (XPC.XPCRichError) -> () in implicit closure #3 (A) -> (XPC.XPCRichError) -> () in XPC.XPCListener.IncomingSessionRequest.accept<A where A: XPC.XPCPeerHandler, A.Input == XPC.XPCReceivedMessage, A.Output == Swift.Encodable>((XPC.XPCSession) -> A
0x1946c10e8  __TEXT,__text  XPC.XPCListener.activate() throws -> ()
0x1946c126c  __TEXT,__text  __swift_xpc_listener_activate
0x1946c12a8  __TEXT,__text  XPC.XPCSession.setTargetQueue(__C.OS_dispatch_queue) -> ()
0x1946c12d0  __TEXT,__text  __swift_xpc_session_set_target_queue
0x1946c134c  __TEXT,__text  XPC.XPCListener.IncomingSessionRequest._accept((XPC.XPCSession) -> ()) -> XPC.XPCListener.IncomingSessionRequest.Decision
0x1946c13a4  __TEXT,__text  _block_destroy_helper.35
0x1946c13a8  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.UInt32?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946c13c4  __TEXT,__text  XPC.XPCSession.setIncomingMessageHandler<A where A: Swift.Decodable>((A) -> Swift.Encodable?) -> ()
0x1946c154c  __TEXT,__text  _block_copy_helper.34
0x1946c1550  __TEXT,__text  XPC.XPCListener.setIncomingSessionHandler(@Sendable (XPC.XPCListener.IncomingSessionRequest) -> XPC.XPCListener.IncomingSessionRequest.Decision) -> ()
0x1946c1680  __TEXT,__text  ___swift_closure_destructor.36
0x1946c1684  __TEXT,__text  ___swift_closure_destructor.40
0x1946c1688  __TEXT,__text  __swift_xpc_listener_set_peer_requirement
0x1946c16d8  __TEXT,__text  __swift_xpc_listener_set_incoming_session_handler
0x1946c1728  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) with unmang
0x1946c1728  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) with unmang
0x1946c1728  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) with unmang
0x1946c1728  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) with unmang
0x1946c1728  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) with unmang
0x1946c1728  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) with unmang
0x1946c1728  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.String, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) with unmang
0x1946c175c  __TEXT,__text  _block_destroy_helper.44
0x1946c1760  __TEXT,__text  lazy protocol witness table accessor for type XPC.XPCRichError and conformance XPC.XPCRichError : Swift.Error in XPC
0x1946c17b4  __TEXT,__text  ___swift_closure_destructor.68
0x1946c17b8  __TEXT,__text  generic specialization <Swift.String> of closure #1 ((key: Swift.String, value: __C.OS_xpc_object)) throws -> () in XPC.XPCDictionary.map<A>(((key: Swift.String, value: __C.OS_xpc_object)) throws -> A) throws -> [A]
0x1946c18b0  __TEXT,__text  generic specialization <Swift.String> of XPC.XPCDictionary.map<A>(((key: Swift.String, value: __C.OS_xpc_object)) throws -> A) throws -> [A]
0x1946c1a3c  __TEXT,__text  generic specialization <Swift.String> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x1946c1b40  __TEXT,__text  partial apply forwarder for generic specialization <Swift.String> of closure #1 ((key: Swift.String, value: __C.OS_xpc_object)) throws -> () in XPC.XPCDictionary.map<A>(((key: Swift.String, value: __C.OS_xpc_object)) throws -> A) throws -> [A]
0x1946c1b60  __TEXT,__text  function signature specialization <Arg[3] = [Constant Propagated KeyPath : a168a102879cc1a6a91172b0770f0c91<(key: Swift.String, value: __C.OS_xpc_object),Swift.String>]> of implicit closure #1 ((key: Swift.String, value: __C.OS_xpc_object)) -> Swift.String in XPC.XPCDictionary.keys.getter : [Swift.S
0x1946c1cc0  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@unowned Swift.Int, @guaranteed __C.OS_xpc_object) -> (@unowned Swift.Bool) to @escaping @callee_guaranteed (@unowned Swift.Int, @guaranteed __C.OS_xpc_object) -> (@unowned Swift.Bool) with unmangled suffix ".62"
0x1946c1cc4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@unowned Swift.Int, @guaranteed __C.OS_xpc_object) -> (@unowned Swift.Bool) to @escaping @callee_guaranteed (@unowned Swift.Int, @guaranteed __C.OS_xpc_object) -> (@unowned Swift.Bool)
0x1946c1cf0  __TEXT,__text  ___swift_closure_destructor.108Tm
0x1946c1d64  __TEXT,__text  ___swift_closure_destructor.108
0x1946c1d68  __TEXT,__text  ___swift_closure_destructor.129
0x1946c1d6c  __TEXT,__text  _block_destroy_helper.132
0x1946c1d70  __TEXT,__text  ___swift_closure_destructor.126
0x1946c1d74  __TEXT,__text  _block_destroy_helper.60
0x1946c1d78  __TEXT,__text  ___swift_closure_destructor.52
0x1946c1d7c  __TEXT,__text  ___swift_closure_destructor.56
0x1946c1d80  __TEXT,__text  ___swift_closure_destructor.28
0x1946c1d84  __TEXT,__text  ___swift_closure_destructor.31
0x1946c1d88  __TEXT,__text  partial apply forwarder for closure #1 (Swift.Int, __C.OS_xpc_object) -> Swift.Bool in closure #1 ((Swift.Int, __C.OS_xpc_object) throws -> ()) throws -> () in XPC.XPCArray.forEach((Swift.Int, __C.OS_xpc_object) throws -> ()) throws -> ()
0x1946c1de4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@unowned Swift.Int, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@unowned Swift.Int, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error)
0x1946c1de4  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@unowned Swift.Int, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error) to @escaping @callee_guaranteed (@unowned Swift.Int, @guaranteed __C.OS_xpc_object) -> (@error @owned Swift.Error)
0x1946c1e74  __TEXT,__text  _block_copy_helper.63
0x1946c1e78  __TEXT,__text  _block_copy_helper.63
0x1946c1ef4  __TEXT,__text  closure #1 ((Swift.Int, __C.OS_xpc_object) throws -> ()) throws -> () in XPC.XPCArray.forEach((Swift.Int, __C.OS_xpc_object) throws -> ()) throws -> ()
0x1946c206c  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed (@unowned Swift.Int, @guaranteed __C.OS_xpc_object) -> (@unowned Swift.Bool) to @callee_unowned @convention(block) (@unowned Swift.Int, @unowned __C.OS_xpc_object) -> (@unowned Swift.Bool)
0x1946c2244  __TEXT,__text  lazy protocol witness table accessor for type Swift.Int64 and conformance Swift.Int64 : Swift.BinaryInteger in Swift
0x1946c2298  __TEXT,__text  closure #1 (XPC.XPCReceivedMessage) -> Swift.Encodable? in XPC.XPCSession.setIncomingMessageHandler<A where A: Swift.Decodable>((A) -> Swift.Encodable?) -> ()
0x1946c24f0  __TEXT,__text  _block_destroy_helper.64
0x1946c24f4  __TEXT,__text  _block_destroy_helper.64
0x1946c24f8  __TEXT,__text  ___swift_closure_destructor.60
0x1946c24fc  __TEXT,__text  ___swift_closure_destructor.25
0x1946c2528  __TEXT,__text  ___swift_closure_destructor.13
0x1946c2538  __TEXT,__text  ___swift_closure_destructor.57
0x1946c2564  __TEXT,__text  ___swift_closure_destructor.57
0x1946c2568  __TEXT,__text  ___swift_closure_destructor.5
0x1946c256c  __TEXT,__text  ___swift_closure_destructor.5
0x1946c2570  __TEXT,__text  ___swift_closure_destructor.5
0x1946c2574  __TEXT,__text  partial apply forwarder for closure #1 (XPC.XPCReceivedMessage) -> Swift.Encodable? in XPC.XPCSession.setIncomingMessageHandler<A where A: Swift.Decodable>((A) -> Swift.Encodable?) -> ()
0x1946c2580  __TEXT,__text  protocol witness for Swift.CustomDebugStringConvertible.debugDescription.getter : Swift.String in conformance XPC.XPCSession : Swift.CustomDebugStringConvertible in XPC
0x1946c25f0  __TEXT,__text  __swift_xpc_session_copy_description
0x1946c2634  __TEXT,__text  function signature specialization <Arg[0] = Exploded> of XPC._SingleValueEncodingContainer.encodeNil() throws -> ()
0x1946c274c  __TEXT,__text  _block_destroy_helper.22
0x1946c2750  __TEXT,__text  ___swift_closure_destructor.19
0x1946c2754  __TEXT,__text  ___swift_closure_destructor.16
0x1946c2758  __TEXT,__text  ___swift_closure_destructor.16
0x1946c275c  __TEXT,__text  associated type witness table accessor for XPC._EncodingContainer.Container : XPC.EncodingGraph.Container in XPC._UnkeyedEncodingContainer : XPC._EncodingContainer in XPC
0x1946c278c  __TEXT,__text  generic specialization <serialized, Swift.UInt8> of Swift._ContiguousArrayBuffer.init(_uninitializedCount: Swift.Int, minimumCapacity: Swift.Int) -> Swift._ContiguousArrayBuffer<A>
0x1946c2b98  __TEXT,__text  ___swift_closure_destructor.113
0x1946c2bbc  __TEXT,__text  __swift_xpc_connection_invalid
0x1946c2be4  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.Int?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946c2bfc  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Double.Type, forKey: A.Key) throws -> Swift.Double? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c3754  __TEXT,__text  protocol witness for Swift.ExpressibleByArrayLiteral.init(arrayLiteral: A.ArrayLiteralElement...) -> A in conformance XPC.xpc_session_create_flags_t : Swift.ExpressibleByArrayLiteral in XPC
0x1946c3774  __TEXT,__text  type metadata accessor for __C.xpc_session_create_flags_t
0x1946c37c4  __TEXT,__text  ___swift_memcpy40_8
0x1946c37d8  __TEXT,__text  getEnumTagSinglePayload value witness for XPC._TopLevelDecoder
0x1946c381c  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC._TopLevelDecoder
0x1946c3864  __TEXT,__text  type metadata accessor for XPC._TopLevelDecoder
0x1946c3874  __TEXT,__text  ___swift_deallocate_boxed_opaque_existential_1
0x1946c38b0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c38b0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c38b0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c38b0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c38b0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c38f4  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c38f4  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c38f4  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c38f4  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c38f4  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC._KeyedDecodingContainer
0x1946c3934  __TEXT,__text  associated type witness table accessor for Swift.KeyedDecodingContainerProtocol.Key : Swift.CodingKey in XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c3934  __TEXT,__text  associated type witness table accessor for Swift.KeyedDecodingContainerProtocol.Key : Swift.CodingKey in XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c393c  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.Int.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Int
0x1946c3970  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.Int8.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Int8
0x1946c39a4  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.Int16.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Int16
0x1946c39d8  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.Int32.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Int32
0x1946c3a0c  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.Int64.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Int64
0x1946c3a40  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.UInt.Type, forKey: A) throws(Swift.DecodingError) -> Swift.UInt
0x1946c3a74  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.UInt8.Type, forKey: A) throws(Swift.DecodingError) -> Swift.UInt8
0x1946c3aa8  __TEXT,__text  merged XPC._KeyedDecodingContainer.decode(_: Swift.Int8.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Int8
0x1946c3ccc  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.UInt16.Type, forKey: A) throws(Swift.DecodingError) -> Swift.UInt16
0x1946c3d00  __TEXT,__text  merged XPC._KeyedDecodingContainer.decode(_: Swift.Int16.Type, forKey: A) throws(Swift.DecodingError) -> Swift.Int16
0x1946c3f24  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.UInt32.Type, forKey: A) throws(Swift.DecodingError) -> Swift.UInt32
0x1946c3f58  __TEXT,__text  XPC._KeyedDecodingContainer.decode(_: Swift.UInt64.Type, forKey: A) throws(Swift.DecodingError) -> Swift.UInt64
0x1946c3f8c  __TEXT,__text  XPC._KeyedDecodingContainer.superDecoder() throws -> Swift.Decoder
0x1946c41d0  __TEXT,__text  XPC._KeyedDecodingContainer.superDecoder(forKey: A) throws(Swift.DecodingError) -> Swift.Decoder
0x1946c4404  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int8.Type, forKey: A.Key) throws -> Swift.Int8 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c4430  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int16.Type, forKey: A.Key) throws -> Swift.Int16 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c445c  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int128.Type, forKey: A.Key) throws -> Swift.Int128 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c4474  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.UInt8.Type, forKey: A.Key) throws -> Swift.UInt8 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c44a0  __TEXT,__text  merged protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int8.Type, forKey: A.Key) throws -> Swift.Int8 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c45b0  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.UInt16.Type, forKey: A.Key) throws -> Swift.UInt16 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c45dc  __TEXT,__text  merged protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.Int16.Type, forKey: A.Key) throws -> Swift.Int16 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c46ec  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decode(_: Swift.UInt128.Type, forKey: A.Key) throws -> Swift.UInt128 in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c4704  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Int8.Type, forKey: A.Key) throws -> Swift.Int8? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c471c  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Int16.Type, forKey: A.Key) throws -> Swift.Int16? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c4738  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Int128.Type, forKey: A.Key) throws -> Swift.Int128? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c4764  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.UInt.Type, forKey: A.Key) throws -> Swift.UInt? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c477c  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.UInt8.Type, forKey: A.Key) throws -> Swift.UInt8? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c4794  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.UInt16.Type, forKey: A.Key) throws -> Swift.UInt16? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c47b0  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.UInt32.Type, forKey: A.Key) throws -> Swift.UInt32? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c47cc  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.UInt64.Type, forKey: A.Key) throws -> Swift.UInt64? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c47e4  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.UInt128.Type, forKey: A.Key) throws -> Swift.UInt128? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c4810  __TEXT,__text  merged protocol witness for Swift.KeyedDecodingContainerProtocol.decodeIfPresent(_: Swift.Int128.Type, forKey: A.Key) throws -> Swift.Int128? in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c4838  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.superDecoder() throws -> Swift.Decoder in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c4860  __TEXT,__text  protocol witness for Swift.KeyedDecodingContainerProtocol.superDecoder(forKey: A.Key) throws -> Swift.Decoder in conformance XPC._KeyedDecodingContainer<A> : Swift.KeyedDecodingContainerProtocol in XPC
0x1946c488c  __TEXT,__text  dispatch thunk of XPC._SingleValueDecodingContainerCommon.encodedValue.getter : XPC.EncodingGraph.Value
0x1946c48a0  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Bool.Type) throws(Swift.DecodingError) -> Swift.Bool
0x1946c48e8  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Double.Type) throws(Swift.DecodingError) -> Swift.Double
0x1946c492c  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Float.Type) throws -> Swift.Float in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946c4970  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Float.Type) throws(Swift.DecodingError) -> Swift.Float
0x1946c49b4  __TEXT,__text  merged generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Float.Type) throws(Swift.DecodingError) -> Swift.Float
0x1946c4b54  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int8.Type) throws -> Swift.Int8 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946c4b94  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int8.Type) throws(Swift.DecodingError) -> Swift.Int8
0x1946c4bc0  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int16.Type) throws(Swift.DecodingError) -> Swift.Int16
0x1946c4bec  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int32.Type) throws -> Swift.Int32 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946c4c2c  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int32.Type) throws(Swift.DecodingError) -> Swift.Int32
0x1946c4c58  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int64.Type) throws -> Swift.Int64 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946c4c84  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int64.Type) throws(Swift.DecodingError) -> Swift.Int64
0x1946c4e04  __TEXT,__text  generic specialization <XPC._SingleValueDecodingContainer> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int64.Type) throws(Swift.DecodingError) -> Swift.Int64
0x1946c4f84  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt.Type) throws -> Swift.UInt in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946c4fb0  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt.Type) throws(Swift.DecodingError) -> Swift.UInt
0x1946c5130  __TEXT,__text  generic specialization <XPC._SingleValueDecodingContainer> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt.Type) throws(Swift.DecodingError) -> Swift.UInt
0x1946c52b0  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt8.Type) throws(Swift.DecodingError) -> Swift.UInt8
0x1946c52dc  __TEXT,__text  merged generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int8.Type) throws(Swift.DecodingError) -> Swift.Int8
0x1946c546c  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt16.Type) throws -> Swift.UInt16 in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946c54ac  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt16.Type) throws(Swift.DecodingError) -> Swift.UInt16
0x1946c54d8  __TEXT,__text  merged generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int16.Type) throws(Swift.DecodingError) -> Swift.Int16
0x1946c5668  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt32.Type) throws(Swift.DecodingError) -> Swift.UInt32
0x1946c5694  __TEXT,__text  merged generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.Int32.Type) throws(Swift.DecodingError) -> Swift.Int32
0x1946c5824  __TEXT,__text  generic specialization <XPC.SingleValueDecodingContainer4OptionalPrimitive> of (extension in XPC):XPC._SingleValueDecodingContainerCommon.decode(Swift.UInt64.Type) throws(Swift.DecodingError) -> Swift.UInt64
0x1946c59a4  __TEXT,__text  protocol witness for XPC._DecodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> A in conformance XPC._SingleValueDecodingContainer : XPC._DecodingContainer in XPC
0x1946c59d8  __TEXT,__text  ___swift_memcpy49_8
0x1946c59f4  __TEXT,__text  type metadata accessor for XPC._SingleValueDecodingContainer
0x1946c5a04  __TEXT,__text  XPC.SingleValueDecodingContainer4OptionalPrimitive.decode<A where A: Swift.Decodable>(A.Type) throws -> A
0x1946c5b84  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Bool.Type) throws -> Swift.Bool in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5bcc  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.String.Type) throws -> Swift.String in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5c10  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Double.Type) throws -> Swift.Double in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5c54  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Float.Type) throws -> Swift.Float in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5c98  __TEXT,__text  merged protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Float.Type) throws -> Swift.Float in conformance XPC._SingleValueDecodingContainer : Swift.SingleValueDecodingContainer in XPC
0x1946c5dcc  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int.Type) throws -> Swift.Int in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5df8  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int8.Type) throws -> Swift.Int8 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5e38  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int16.Type) throws -> Swift.Int16 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5e78  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int32.Type) throws -> Swift.Int32 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5eb8  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int64.Type) throws -> Swift.Int64 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5ee4  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt.Type) throws -> Swift.UInt in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5f10  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt8.Type) throws -> Swift.UInt8 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5f50  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt16.Type) throws -> Swift.UInt16 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5f90  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt32.Type) throws -> Swift.UInt32 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5fd0  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt64.Type) throws -> Swift.UInt64 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c5ffc  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode<A where A1: Swift.Decodable>(A1.Type) throws -> A1 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c6014  __TEXT,__text  protocol witness for XPC._DecodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> A in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : XPC._DecodingContainer in XPC
0x1946c6048  __TEXT,__text  merged protocol witness for XPC._DecodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container) throws(Swift.DecodingError) -> A in conformance XPC._SingleValueDecodingContainer : XPC._DecodingContainer in XPC
0x1946c615c  __TEXT,__text  merged getEnumTagSinglePayload value witness for XPC._SingleValueDecodingContainer
0x1946c61a0  __TEXT,__text  merged storeEnumTagSinglePayload value witness for XPC._SingleValueDecodingContainer
0x1946c61ec  __TEXT,__text  type metadata accessor for XPC.SingleValueDecodingContainer4OptionalPrimitive
0x1946c61fc  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.codingPath.getter : [Swift.CodingKey] in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c61fc  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.codingPath.getter : [Swift.CodingKey] in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c6200  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int128.Type) throws -> Swift.Int128 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c6200  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.Int128.Type) throws -> Swift.Int128 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c6218  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt128.Type) throws -> Swift.UInt128 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c6218  __TEXT,__text  protocol witness for Swift.SingleValueDecodingContainer.decode(Swift.UInt128.Type) throws -> Swift.UInt128 in conformance XPC.SingleValueDecodingContainer4OptionalPrimitive : Swift.SingleValueDecodingContainer in XPC
0x1946c6230  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.SingleValueDecodingContainer4OptionalPrimitive
0x1946c6230  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.SingleValueDecodingContainer4OptionalPrimitive
0x1946c6234  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.SingleValueDecodingContainer4OptionalPrimitive
0x1946c6234  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.SingleValueDecodingContainer4OptionalPrimitive
0x1946c6238  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.String.Type) throws(Swift.DecodingError) -> Swift.String
0x1946c6530  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.Float.Type) throws(Swift.DecodingError) -> Swift.Float
0x1946c6828  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.Double.Type) throws(Swift.DecodingError) -> Swift.Double
0x1946c6b20  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.Int.Type) throws(Swift.DecodingError) -> Swift.Int
0x1946c6b4c  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.Int8.Type) throws(Swift.DecodingError) -> Swift.Int8
0x1946c6b78  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.Int16.Type) throws(Swift.DecodingError) -> Swift.Int16
0x1946c6ba4  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.Int32.Type) throws(Swift.DecodingError) -> Swift.Int32
0x1946c6bd0  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.Int64.Type) throws(Swift.DecodingError) -> Swift.Int64
0x1946c6bfc  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.UInt.Type) throws(Swift.DecodingError) -> Swift.UInt
0x1946c6c28  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.UInt8.Type) throws(Swift.DecodingError) -> Swift.UInt8
0x1946c6c54  __TEXT,__text  merged XPC._UnkeyedDecodingContainer.decode(Swift.Int8.Type) throws(Swift.DecodingError) -> Swift.Int8
0x1946c6f50  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.UInt16.Type) throws(Swift.DecodingError) -> Swift.UInt16
0x1946c6f7c  __TEXT,__text  merged XPC._UnkeyedDecodingContainer.decode(Swift.Int16.Type) throws(Swift.DecodingError) -> Swift.Int16
0x1946c7278  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.UInt32.Type) throws(Swift.DecodingError) -> Swift.UInt32
0x1946c72a4  __TEXT,__text  merged XPC._UnkeyedDecodingContainer.decode(Swift.Int32.Type) throws(Swift.DecodingError) -> Swift.Int32
0x1946c75a0  __TEXT,__text  XPC._UnkeyedDecodingContainer.decode(Swift.UInt64.Type) throws(Swift.DecodingError) -> Swift.UInt64
0x1946c75cc  __TEXT,__text  generic specialization <XPC._UnkeyedDecodingContainer> of XPC._UnkeyedDecodingContainer.(_container in _1016890FE93F2D24F6CF826DE25716D5)<A where A: XPC._DecodingContainer>(_: A.Type, forType: Any.Type?) throws(Swift.DecodingError) -> A
0x1946c7968  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.currentIndex.getter : Swift.Int in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7970  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.String.Type) throws -> Swift.String in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7a54  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Double.Type) throws -> Swift.Double in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7b38  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Float.Type) throws -> Swift.Float in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7c1c  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int8.Type) throws -> Swift.Int8 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7c48  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int16.Type) throws -> Swift.Int16 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7c74  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int32.Type) throws -> Swift.Int32 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7ca0  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int64.Type) throws -> Swift.Int64 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7ccc  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int128.Type) throws -> Swift.Int128 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7ce4  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.UInt.Type) throws -> Swift.UInt in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7d10  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.UInt8.Type) throws -> Swift.UInt8 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7d3c  __TEXT,__text  merged protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int8.Type) throws -> Swift.Int8 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7e28  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.UInt16.Type) throws -> Swift.UInt16 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7e54  __TEXT,__text  merged protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int16.Type) throws -> Swift.Int16 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7f40  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.UInt32.Type) throws -> Swift.UInt32 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c7f6c  __TEXT,__text  merged protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.Int32.Type) throws -> Swift.Int32 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8058  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decode(Swift.UInt128.Type) throws -> Swift.UInt128 in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8070  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Bool.Type) throws -> Swift.Bool? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8088  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.String.Type) throws -> Swift.String? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c80a0  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Double.Type) throws -> Swift.Double? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c80b8  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Float.Type) throws -> Swift.Float? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c80d4  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Int.Type) throws -> Swift.Int? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c80ec  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Int8.Type) throws -> Swift.Int8? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8104  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Int16.Type) throws -> Swift.Int16? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8120  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Int32.Type) throws -> Swift.Int32? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c813c  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Int64.Type) throws -> Swift.Int64? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8154  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Int128.Type) throws -> Swift.Int128? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8180  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.UInt.Type) throws -> Swift.UInt? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8198  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.UInt8.Type) throws -> Swift.UInt8? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c81b0  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.UInt16.Type) throws -> Swift.UInt16? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c81cc  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.UInt32.Type) throws -> Swift.UInt32? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c81e8  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.UInt64.Type) throws -> Swift.UInt64? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8200  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.UInt128.Type) throws -> Swift.UInt128? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c822c  __TEXT,__text  merged protocol witness for Swift.UnkeyedDecodingContainer.decodeIfPresent(Swift.Int128.Type) throws -> Swift.Int128? in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8254  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.nestedUnkeyedContainer() throws -> Swift.UnkeyedDecodingContainer in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c8378  __TEXT,__text  protocol witness for Swift.UnkeyedDecodingContainer.superDecoder() throws -> Swift.Decoder in conformance XPC._UnkeyedDecodingContainer : Swift.UnkeyedDecodingContainer in XPC
0x1946c84c4  __TEXT,__text  ___swift_memcpy64_8
0x1946c84d8  __TEXT,__text  getEnumTagSinglePayload value witness for XPC._UnkeyedDecodingContainer
0x1946c851c  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC._UnkeyedDecodingContainer
0x1946c856c  __TEXT,__text  type metadata accessor for XPC._UnkeyedDecodingContainer
0x1946c859c  __TEXT,__text  protocol witness for XPC._EncodingContainer.codingInfo.getter : XPC.CodingInfo in conformance XPC._TopLevelEncoder : XPC._EncodingContainer in XPC
0x1946cb05c  __TEXT,__text  Swift._StringGuts._slowEnsureMatchingEncoding(Swift.String.Index) -> Swift.String.Index
0x1946cb0f0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCEncodedContents
0x1946cb0f0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCEncodedContents
0x1946cb134  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCEncodedContents
0x1946cb134  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.XPCEncodedContents
0x1946cb184  __TEXT,__text  type metadata accessor for XPC._TopLevelEncoder
0x1946cb194  __TEXT,__text  XPC._KeyedEncodingContainer.encodeNil(forKey: A) throws -> ()
0x1946cb1f4  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.Int8, forKey: A) throws -> ()
0x1946cb21c  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.Int16, forKey: A) throws -> ()
0x1946cb244  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.Int32, forKey: A) throws -> ()
0x1946cb26c  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.UInt8, forKey: A) throws -> ()
0x1946cb294  __TEXT,__text  merged XPC._KeyedEncodingContainer.encode(_: Swift.Int8, forKey: A) throws -> ()
0x1946cb2dc  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.UInt16, forKey: A) throws -> ()
0x1946cb304  __TEXT,__text  merged XPC._KeyedEncodingContainer.encode(_: Swift.Int16, forKey: A) throws -> ()
0x1946cb34c  __TEXT,__text  XPC._KeyedEncodingContainer.encode(_: Swift.UInt32, forKey: A) throws -> ()
0x1946cb374  __TEXT,__text  XPC._KeyedEncodingContainer._ContainerCodingKey.init(stringValue: Swift.String) -> XPC._KeyedEncodingContainer<A>._ContainerCodingKey?
0x1946cb3d0  __TEXT,__text  XPC._KeyedEncodingContainer._ContainerCodingKey.init(intValue: Swift.Int) -> XPC._KeyedEncodingContainer<A>._ContainerCodingKey?
0x1946cb42c  __TEXT,__text  XPC._KeyedEncodingContainer._ContainerCodingKey.stringValue.getter : Swift.String
0x1946cb4f4  __TEXT,__text  XPC._KeyedEncodingContainer._ContainerCodingKey.intValue.getter : Swift.Int?
0x1946cb574  __TEXT,__text  protocol witness for Swift.CodingKey.stringValue.getter : Swift.String in conformance XPC._KeyedEncodingContainer<A>._ContainerCodingKey : Swift.CodingKey in XPC
0x1946cb578  __TEXT,__text  protocol witness for Swift.CodingKey.init(stringValue: Swift.String) -> A? in conformance XPC._KeyedEncodingContainer<A>._ContainerCodingKey : Swift.CodingKey in XPC
0x1946cb588  __TEXT,__text  protocol witness for Swift.CodingKey.intValue.getter : Swift.Int? in conformance XPC._KeyedEncodingContainer<A>._ContainerCodingKey : Swift.CodingKey in XPC
0x1946cb58c  __TEXT,__text  protocol witness for Swift.CodingKey.init(intValue: Swift.Int) -> A? in conformance XPC._KeyedEncodingContainer<A>._ContainerCodingKey : Swift.CodingKey in XPC
0x1946cb59c  __TEXT,__text  protocol witness for Swift.CustomStringConvertible.description.getter : Swift.String in conformance XPC._KeyedEncodingContainer<A>._ContainerCodingKey : Swift.CustomStringConvertible in XPC
0x1946cb5e4  __TEXT,__text  protocol witness for Swift.CustomDebugStringConvertible.debugDescription.getter : Swift.String in conformance XPC._KeyedEncodingContainer<A>._ContainerCodingKey : Swift.CustomDebugStringConvertible in XPC
0x1946cb62c  __TEXT,__text  XPC._KeyedEncodingContainer.nestedUnkeyedContainer(forKey: A) -> Swift.UnkeyedEncodingContainer
0x1946cb67c  __TEXT,__text  XPC._KeyedEncodingContainer.superEncoder() -> Swift.Encoder
0x1946cb7f8  __TEXT,__text  XPC._KeyedEncodingContainer.superEncoder(forKey: A) -> Swift.Encoder
0x1946cb848  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.codingPath.getter : [Swift.CodingKey] in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb854  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeNil(forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb87c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int8, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb898  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int16, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb8b4  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int128, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb8cc  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.UInt8, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb8e8  __TEXT,__text  merged protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int8, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb920  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.UInt16, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb93c  __TEXT,__text  merged protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.Int16, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb974  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encode(_: Swift.UInt128, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb98c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeConditional<A where A1: AnyObject, A1: Swift.Encodable>(_: A1, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb9b8  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.Double?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb9d0  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.Int8?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cb9e8  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.Int16?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cba04  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.Int128?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cba1c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.UInt?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cba34  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.UInt8?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cba4c  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.UInt16?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cba68  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.UInt64?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cba80  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.encodeIfPresent(_: Swift.UInt128?, forKey: A.Key) throws -> () in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cba98  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.superEncoder() -> Swift.Encoder in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cbaac  __TEXT,__text  protocol witness for Swift.KeyedEncodingContainerProtocol.superEncoder(forKey: A.Key) -> Swift.Encoder in conformance XPC._KeyedEncodingContainer<A> : Swift.KeyedEncodingContainerProtocol in XPC
0x1946cbadc  __TEXT,__text  generic specialization <XPC.EncodingGraph.Value> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x1946cbaf0  __TEXT,__text  getEnumTagSinglePayload value witness for XPC._KeyedEncodingContainer._ContainerCodingKey
0x1946cbc4c  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC._KeyedEncodingContainer._ContainerCodingKey
0x1946cbe40  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.Float) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946cbe5c  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.Int8) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946cbe7c  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.Int32) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946cbe9c  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.Int64) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946cbebc  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.Int128) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946cbed4  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.UInt) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946cbef4  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.UInt16) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946cbf14  __TEXT,__text  protocol witness for Swift.SingleValueEncodingContainer.encode(Swift.UInt128) throws -> () in conformance XPC._SingleValueEncodingContainer : Swift.SingleValueEncodingContainer in XPC
0x1946cbf2c  __TEXT,__text  protocol witness for XPC._EncodingContainer.init(codingInfo: XPC.CodingInfo, container: XPC.EncodingGraph.Container?) -> A in conformance XPC._SingleValueEncodingContainer : XPC._EncodingContainer in XPC
0x1946cbfb4  __TEXT,__text  type metadata accessor for XPC._SingleValueEncodingContainer
0x1946cbfc4  __TEXT,__text  associated type witness table accessor for XPC._EncodingContainer.Container : XPC.EncodingGraph.Container in XPC._SingleValueEncodingContainer : XPC._EncodingContainer in XPC
0x1946cbfd0  __TEXT,__text  function signature specialization <Arg[1] = Exploded> of XPC._SingleValueEncodingContainer.encode(Swift.Float) throws -> ()
0x1946cc0f8  __TEXT,__text  generic specialization <XPC._UnkeyedEncodingContainer> of XPC._UnkeyedEncodingContainer._encodingContainer<A where A: XPC._EncodingContainer>(_: A.Type, forType: Any.Type?) -> A
0x1946cc29c  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.count.getter : Swift.Int in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc2e0  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encodeNil() throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc3d8  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.String) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc3f4  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Double) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc4f8  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Float) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc600  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int8) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc61c  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int16) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc638  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int32) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc654  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int64) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc670  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int128) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc688  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.UInt) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc6a4  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.UInt8) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc6c0  __TEXT,__text  merged protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int8) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc7c8  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.UInt16) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc7e4  __TEXT,__text  merged protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int16) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc8ec  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.UInt32) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cc908  __TEXT,__text  merged protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.Int32) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cca10  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode(Swift.UInt128) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cca28  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encodeConditional<A where A1: AnyObject, A1: Swift.Encodable>(A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cca54  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.Bool>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cca80  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.String>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccaac  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.Double>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccad8  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.Float>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccb04  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.Int>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccb30  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.Int8>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccb5c  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.Int16>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccb88  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.Int32>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccbb4  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.Int64>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccbe0  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.Int128>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccc0c  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.UInt>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccc38  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.UInt16>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccc64  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.UInt32>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccc90  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.UInt64>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cccbc  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element == Swift.UInt128>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccce8  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.encode<A where A1: Swift.Sequence, A1.Element: Swift.Encodable>(contentsOf: A1) throws -> () in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccd1c  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.nestedUnkeyedContainer() -> Swift.UnkeyedEncodingContainer in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946ccd94  __TEXT,__text  protocol witness for Swift.UnkeyedEncodingContainer.superEncoder() -> Swift.Encoder in conformance XPC._UnkeyedEncodingContainer : Swift.UnkeyedEncodingContainer in XPC
0x1946cce1c  __TEXT,__text  type metadata accessor for XPC._UnkeyedEncodingContainer
0x1946cce2c  __TEXT,__text  protocol witness for Swift.CodingKey.stringValue.getter : Swift.String in conformance XPC.IndexCodingKey : Swift.CodingKey in XPC
0x1946cce40  __TEXT,__text  protocol witness for Swift.CodingKey.init(stringValue: Swift.String) -> A? in conformance XPC.IndexCodingKey : Swift.CodingKey in XPC
0x1946cce9c  __TEXT,__text  protocol witness for Swift.CodingKey.intValue.getter : Swift.Int? in conformance XPC.IndexCodingKey : Swift.CodingKey in XPC
0x1946ccea8  __TEXT,__text  protocol witness for Swift.CodingKey.init(intValue: Swift.Int) -> A? in conformance XPC.IndexCodingKey : Swift.CodingKey in XPC
0x1946cceb4  __TEXT,__text  protocol witness for Swift.CustomStringConvertible.description.getter : Swift.String in conformance XPC.IndexCodingKey : Swift.CustomStringConvertible in XPC
0x1946ccee4  __TEXT,__text  protocol witness for Swift.CustomDebugStringConvertible.debugDescription.getter : Swift.String in conformance XPC.IndexCodingKey : Swift.CustomDebugStringConvertible in XPC
0x1946ccf14  __TEXT,__text  ___swift_exist.box.addr_destructor.8
0x1946ccf50  __TEXT,__text  function signature specialization <Arg[1] = Exploded> of XPC._UnkeyedEncodingContainer.encode(Swift.String) throws -> ()
0x1946cd07c  __TEXT,__text  type metadata accessor for XPC.IndexCodingKey
0x1946cd324  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.CodingUserInfoKeyNotFound
0x1946cd338  __TEXT,__text  storeEnumTagSinglePayload value witness for XPC.CodingUserInfoKeyNotFound
0x1946cd34c  __TEXT,__text  type metadata accessor for XPC.CodingUserInfoKeyNotFound
0x1946cd398  __TEXT,__text  type metadata completion function for XPC.CodingUserInfoKeyNotFound
0x1946cd404  __TEXT,__text  protocol witness for Swift.Error._getEmbeddedNSError() -> Swift.AnyObject? in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946cd404  __TEXT,__text  protocol witness for Swift.Error._getEmbeddedNSError() -> Swift.AnyObject? in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946cd404  __TEXT,__text  protocol witness for Swift.Error._getEmbeddedNSError() -> Swift.AnyObject? in conformance XPC.CodingUserInfoKeyNotFound : Swift.Error in XPC
0x1946cd408  __TEXT,__text  protocol witness for Swift.CustomDebugStringConvertible.debugDescription.getter : Swift.String in conformance XPC.CodingUserInfoKeyNotFound : Swift.CustomDebugStringConvertible in XPC
0x1946cd52c  __TEXT,__text  getEnumTagSinglePayload value witness for XPC.XPCData
```
First 1,000 of 1,486.

