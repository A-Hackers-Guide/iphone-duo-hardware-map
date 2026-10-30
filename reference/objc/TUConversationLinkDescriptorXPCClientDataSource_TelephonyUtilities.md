# `TUConversationLinkDescriptorXPCClientDataSource`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUConversationLinkDescriptorXPCClient`, `TUConversationLinkDescriptorDataSource`, `TUConversationLinkKeyValueDataSource`
- 3 instance variables, 7 properties, 38 instance methods, 6 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accessorLock;
@"<TUConversationLinkDescriptorDataSourceDelegate>" _conversationLinkDescriptorDataSourceDelegate;
@"NSXPCConnection" _xpcConnection;
```

## Properties

```
@property (T{os_unfair_lock_s=I},R,N,V_accessorLock) accessorLock;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<TUConversationLinkDescriptorDataSourceDelegate>",&,N,V_conversationLinkDescriptorDataSourceDelegate) conversationLinkDescriptorDataSourceDelegate;
```

## Class methods

```
+[TUConversationLinkDescriptorXPCClientDataSource setAsynchronousServer:];
+[TUConversationLinkDescriptorXPCClientDataSource asynchronousServer];
+[TUConversationLinkDescriptorXPCClientDataSource setSynchronousServer:];
+[TUConversationLinkDescriptorXPCClientDataSource synchronousServer];
+[TUConversationLinkDescriptorXPCClientDataSource clientXPCInterface];
+[TUConversationLinkDescriptorXPCClientDataSource serverXPCInterface];
```

## Instance methods

```
-[TUConversationLinkDescriptorXPCClientDataSource accessorLock];
-[TUConversationLinkDescriptorXPCClientDataSource synchronousServerWithErrorHandler:];
-[TUConversationLinkDescriptorXPCClientDataSource init];
-[TUConversationLinkDescriptorXPCClientDataSource setXpcConnection:];
-[TUConversationLinkDescriptorXPCClientDataSource dealloc];
-[TUConversationLinkDescriptorXPCClientDataSource xpcConnection];
-[TUConversationLinkDescriptorXPCClientDataSource setInteger:forKey:error:];
-[TUConversationLinkDescriptorXPCClientDataSource integerForKey:error:];
-[TUConversationLinkDescriptorXPCClientDataSource asynchronousServerWithErrorHandler:];
-[TUConversationLinkDescriptorXPCClientDataSource setString:forKey:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource setString:forKey:error:];
-[TUConversationLinkDescriptorXPCClientDataSource stringForKey:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource stringForKey:error:];
-[TUConversationLinkDescriptorXPCClientDataSource addConversationLinkDescriptors:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource addConversationLinkDescriptors:error:];
-[TUConversationLinkDescriptorXPCClientDataSource addOrUpdateConversationLinkDescriptors:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource addOrUpdateConversationLinkDescriptors:error:];
-[TUConversationLinkDescriptorXPCClientDataSource conversationLinkDescriptorCountWithPredicate:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource conversationLinkDescriptorCountWithPredicate:error:];
-[TUConversationLinkDescriptorXPCClientDataSource conversationLinkDescriptorDataSourceDelegate];
-[TUConversationLinkDescriptorXPCClientDataSource conversationLinkDescriptorsDidChange];
-[TUConversationLinkDescriptorXPCClientDataSource conversationLinkDescriptorsWithPredicate:limit:offset:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource conversationLinkDescriptorsWithPredicate:limit:offset:error:];
-[TUConversationLinkDescriptorXPCClientDataSource integerForKey:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource removeConversationLinkDescriptorsWithPredicate:deleteReason:deletionLayer:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource removeConversationLinkDescriptorsWithPredicate:deleteReason:deletionLayer:error:];
-[TUConversationLinkDescriptorXPCClientDataSource removeLinkDescriptorsFromDataSourceWithPredicate:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource removeLinkDescriptorsFromDataSourceWithPredicate:error:];
-[TUConversationLinkDescriptorXPCClientDataSource setActivated:withRevision:forConversationLinkDescriptorsWithPredicate:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource setActivated:withRevision:forConversationLinkDescriptorsWithPredicate:error:];
-[TUConversationLinkDescriptorXPCClientDataSource setConversationLinkDescriptorDataSourceDelegate:];
-[TUConversationLinkDescriptorXPCClientDataSource setExpirationDate:withRevision:forConversationLinkDescriptorsWithPredicate:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource setExpirationDate:withRevision:forConversationLinkDescriptorsWithPredicate:error:];
-[TUConversationLinkDescriptorXPCClientDataSource setInteger:forKey:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource setInvitedHandles:withRevision:forConversationLinkDescriptorsWithPredicate:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource setInvitedHandles:withRevision:forConversationLinkDescriptorsWithPredicate:error:];
-[TUConversationLinkDescriptorXPCClientDataSource setName:withRevision:forConversationLinkDescriptorsWithPredicate:completion:];
-[TUConversationLinkDescriptorXPCClientDataSource setName:withRevision:forConversationLinkDescriptorsWithPredicate:error:];
```
