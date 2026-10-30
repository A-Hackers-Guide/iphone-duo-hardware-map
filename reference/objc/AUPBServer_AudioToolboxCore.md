# `AUPBServer`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `AUPBServing`
- 13 instance variables, 4 properties, 30 instance methods, 2 class methods

## Instance variables

```
@"NSXPCConnection" mRegistrarConnection;
@"<AUPBRegistrarHosting>" mProxyInterface;
@"NSXPCListener" mListener;
@"NSMutableArray" mClientConnections;
{unique_ptr<caulk::mach::unfair_recursive_lock, std::default_delete<caulk::mach::unfair_recursive_lock>>=""{?="__ptr_"^{unfair_recursive_lock}}} mLock;
{map<unsigned int, RemoteAUHandleInfo, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, RemoteAUHandleInfo>>>="__tree_"{__tree<std::__value_type<unsigned int, RemoteAUHandleInfo>, std::__map_value_compare<unsigned int, std::pair<const unsigned int, RemoteAUHandleInfo>, std::less<unsigned int>>, std::allocator<std::pair<const unsigned int, RemoteAUHandleInfo>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} mAUHandlesToInfo;
{map<unsigned int, AUProcessingBlock, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, AUProcessingBlock>>>="__tree_"{__tree<std::__value_type<unsigned int, AUProcessingBlock>, std::__map_value_compare<unsigned int, std::pair<const unsigned int, AUProcessingBlock>, std::less<unsigned int>>, std::allocator<std::pair<const unsigned int, AUProcessingBlock>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} mBlockHandlesToMethods;
I mAUPBRefCounter;
{unique_ptr<TestAUProcessingBlock, std::default_delete<TestAUProcessingBlock>>=""{?="__ptr_"^{TestAUProcessingBlock}}} mTestBlock;
I mAUHandleCntr;
i mNotifyToken;
B mValidToken;
B mConnectionAcknowledged;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AUPBServer sharedInstance];
+[AUPBServer allocWithZone:];
```

## Instance methods

```
-[AUPBServer listener:shouldAcceptNewConnection:];
-[AUPBServer init];
-[AUPBServer dealloc];
-[AUPBServer autorelease];
-[AUPBServer retain];
-[AUPBServer release];
-[AUPBServer retainCount];
-[AUPBServer copyWithZone:];
-[AUPBServer auHandleFromRef:];
-[AUPBServer auRefFromHandle:];
-[AUPBServer aupbFromAUHandle:];
-[AUPBServer aupbFromRef:];
-[AUPBServer blockListChanged];
-[AUPBServer checkConnectRegistrar];
-[AUPBServer copyProcessingBlock:property:intoReply:];
-[AUPBServer getAudioUnit:parameter:onScope:element:inReply:];
-[AUPBServer getAudioUnit:property:onScope:element:inReply:];
-[AUPBServer getAudioUnit:propertyInfo:onScope:element:inReply:];
-[AUPBServer handleFromAUPBRef:];
-[AUPBServer handleRegistrarCrash];
-[AUPBServer processingBlock:properties:count:changedWithQualifierData:length:];
-[AUPBServer processingBlockRef:propertyChanged:];
-[AUPBServer registerAU:inBlock:];
-[AUPBServer registerBlock:withUserData:];
-[AUPBServer setAudioUnit:parameter:onScope:element:value:withReply:];
-[AUPBServer setAudioUnit:property:onScope:element:value:withReply:];
-[AUPBServer setProcessingBlock:property:value:withReply:];
-[AUPBServer startRegistrarConnection];
-[AUPBServer unregisterAU:];
-[AUPBServer unregisterBlock:];
```
