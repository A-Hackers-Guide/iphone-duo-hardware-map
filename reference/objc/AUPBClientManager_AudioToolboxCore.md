# `AUPBClientManager`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AUPBRegistrarListening`, `AUPBInspecting`
- 10 instance variables, 4 properties, 30 instance methods, 2 class methods

## Instance variables

```
@"NSXPCConnection" mRegistrarConnection;
@"<AUPBRegistrarHosting>" mProxyInterface;
@"NSMutableArray" mRemoteServers;
{vector<PropertyListener, std::allocator<PropertyListener>>="__begin_"^{PropertyListener}"__end_"^{PropertyListener}""{?="__cap_"^{PropertyListener}}} mPropertyListeners;
{vector<NewServerListener, std::allocator<NewServerListener>>="__begin_"^{NewServerListener}"__end_"^{NewServerListener}""{?="__cap_"^{NewServerListener}}} mNewServerListeners;
I mServerRefCounter;
@"NSObject<OS_dispatch_queue>" mTouchServersQueue;
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
+[AUPBClientManager sharedInstance];
+[AUPBClientManager allocWithZone:];
```

## Instance methods

```
-[AUPBClientManager init];
-[AUPBClientManager dealloc];
-[AUPBClientManager autorelease];
-[AUPBClientManager retain];
-[AUPBClientManager release];
-[AUPBClientManager retainCount];
-[AUPBClientManager copyWithZone:];
-[AUPBClientManager newServerAdded:];
-[AUPBClientManager addNewServerListener:withUserData:];
-[AUPBClientManager addPropertyListener:onServer:block:property:withUserData:];
-[AUPBClientManager auHandleFromRef:];
-[AUPBClientManager auRefFromHandle:];
-[AUPBClientManager aupbRefFromHandle:];
-[AUPBClientManager copyPBProperty:onServer:block:intoValue:];
-[AUPBClientManager getAUParameter:onServer:audioUnit:scope:element:copiedIntoValue:];
-[AUPBClientManager getAUProperty:onServer:audioUnit:scope:element:copiedIntoBufer:withSize:];
-[AUPBClientManager getAUPropertyInfo:onServer:audioUnit:scope:element:intoDataSize:writeable:];
-[AUPBClientManager getSerialAUProperty:onServer:audioUnit:scope:element:inData:];
-[AUPBClientManager handleRegistrarCrash];
-[AUPBClientManager processingBlock:propertiesChanged:withQualifierData:];
-[AUPBClientManager processingBlock:propertyChanged:];
-[AUPBClientManager removePropertyListener:onServer:block:property:withUserData:];
-[AUPBClientManager removePropertyListenersForServer:];
-[AUPBClientManager removeServerListener:withUserData:];
-[AUPBClientManager serverFromRef:];
-[AUPBClientManager setAUParameter:onServer:audioUnit:scope:element:value:];
-[AUPBClientManager setAUProperty:onServer:audioUnit:scope:element:withValue:size:];
-[AUPBClientManager setPBProperty:onServer:block:value:];
-[AUPBClientManager setSerialAUProperty:onServer:audioUnit:scope:element:toData:];
-[AUPBClientManager startRegistarConnection];
```
