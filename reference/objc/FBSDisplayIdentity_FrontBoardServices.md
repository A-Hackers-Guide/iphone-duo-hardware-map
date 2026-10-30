# `FBSDisplayIdentity`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSSecureCoding`
- 11 instance variables, 12 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"NSString" _uniqueIdentifier;
@"FBSDisplayIdentity" _rootIdentity;
q _type;
q _connectionType;
I _displayID;
I _connectionSeed;
i _pid;
B _mainLike;
B _external;
B _secure;
B _alwaysConnected;
```

## Properties

```
@property (TB,R,N,GisUIKitMainLike,V_mainLike) UIKitMainLike;
@property (Ti,R,N,V_pid) pid;
@property (T@"FBSDisplayIdentity",R,C,N) rootIdentity;
@property (TB,R,N) isRootIdentity;
@property (TB,R,N,GisMainDisplay) mainDisplay;
@property (TB,R,N,GisExternal,V_external) external;
@property (TB,R,N,GisCarDisplay) carDisplay;
@property (TB,R,N,GisCarInstrumentsDisplay) carInstrumentsDisplay;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSDisplayIdentity supportsSecureCoding];
```

## Instance methods

```
-[FBSDisplayIdentity isContinuityDisplay];
-[FBSDisplayIdentity connectionSeed];
-[FBSDisplayIdentity isExternal];
-[FBSDisplayIdentity connectionType];
-[FBSDisplayIdentity debugDescription];
-[FBSDisplayIdentity init];
-[FBSDisplayIdentity isCarDisplay];
-[FBSDisplayIdentity isVirtualized];
-[FBSDisplayIdentity initWithXPCDictionary:];
-[FBSDisplayIdentity _initWithType:UIKitMainLike:displayID:connectionType:connectionSeed:pid:external:uniqueIdentifier:secure:alwaysConnected:root:];
-[FBSDisplayIdentity isUIKitMainLike];
-[FBSDisplayIdentity displayID];
-[FBSDisplayIdentity isRootIdentity];
-[FBSDisplayIdentity uniqueIdentifier];
-[FBSDisplayIdentity isAlwaysConnected];
-[FBSDisplayIdentity pid];
-[FBSDisplayIdentity isMainRootDisplay];
-[FBSDisplayIdentity type];
-[FBSDisplayIdentity encodeWithXPCDictionary:];
-[FBSDisplayIdentity isCarInstrumentsDisplay];
-[FBSDisplayIdentity encodeWithCoder:];
-[FBSDisplayIdentity expectsSecureRendering];
-[FBSDisplayIdentity hash];
-[FBSDisplayIdentity isMainDisplay];
-[FBSDisplayIdentity description];
-[FBSDisplayIdentity initWithCoder:];
-[FBSDisplayIdentity rootIdentity];
-[FBSDisplayIdentity isiPodOnlyDisplay];
-[FBSDisplayIdentity copyWithZone:];
-[FBSDisplayIdentity isEqual:];
-[FBSDisplayIdentity isAirPlayDisplay];
-[FBSDisplayIdentity isRestrictedAirPlayDisplay];
-[FBSDisplayIdentity isMusicOnlyDisplay];
```
