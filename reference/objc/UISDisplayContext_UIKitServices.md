# `UISDisplayContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSMutableCopying`
- 5 instance variables, 9 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"FBSDisplayConfiguration" _displayConfiguration;
@"UISApplicationSupportDisplayEdgeInfo" _displayEdgeInfo;
Q _artworkSubtype;
Q _userInterfaceStyle;
@"UISDisplayShape" _exclusionArea;
```

## Properties

```
@property (T@"FBSDisplayConfiguration",R,N,V_displayConfiguration) displayConfiguration;
@property (T@"UISApplicationSupportDisplayEdgeInfo",R,N,V_displayEdgeInfo) displayEdgeInfo;
@property (TQ,R,N,V_artworkSubtype) artworkSubtype;
@property (TQ,R,N,V_userInterfaceStyle) userInterfaceStyle;
@property (T@"UISDisplayShape",R,N,V_exclusionArea) exclusionArea;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISDisplayContext defaultContext];
```

## Instance methods

```
-[UISDisplayContext displayConfiguration];
-[UISDisplayContext mutableCopyWithZone:];
-[UISDisplayContext initWithXPCDictionary:];
-[UISDisplayContext initWithDisplayConfiguration:];
-[UISDisplayContext userInterfaceStyle];
-[UISDisplayContext encodeWithXPCDictionary:];
-[UISDisplayContext hash];
-[UISDisplayContext description];
-[UISDisplayContext copyWithZone:];
-[UISDisplayContext isEqual:];
-[UISDisplayContext displayEdgeInfo];
-[UISDisplayContext artworkSubtype];
-[UISDisplayContext exclusionArea];
-[UISDisplayContext initWithDisplayConfiguration:displayEdgeInfo:exclusionArea:];
-[UISDisplayContext _initWithDisplayContext:];
-[UISDisplayContext initWithDisplayConfiguration:displayEdgeInfo:];
```
