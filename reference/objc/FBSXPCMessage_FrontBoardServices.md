# `FBSXPCMessage`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 5 instance methods, 4 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _payload;
@"<BSXPCServiceConnectionMessage>" _reply;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",R,N,V_payload) payload;
```

## Class methods

```
+[FBSXPCMessage message];
+[FBSXPCMessage messageWithPayload:];
+[FBSXPCMessage messageWithBSXPCMessage:ownReply:];
+[FBSXPCMessage messageWithPacker:];
```

## Instance methods

```
-[FBSXPCMessage init];
-[FBSXPCMessage initWithMessagePacker:];
-[FBSXPCMessage payload];
-[FBSXPCMessage sendReplyMessageWithPacker:];
-[FBSXPCMessage initWithMessagePayload:];
```
