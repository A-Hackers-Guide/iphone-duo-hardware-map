# `BKSHIDEventDigitizerPathAttributes`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSProtobufSerializable`, `NSCopying`, `BSDescriptionStreamable`
- 11 instance variables, 20 properties, 35 instance methods, 1 class methods

## Instance variables

```
@"BKSHIDEventSimpleProvenance" _simpleProvenance;
C _locus;
I _touchIdentifier;
I _userIdentifier;
f _zGradient;
q _pathIndex;
q _hitTestContextCategory;
@"BKSHIDEventAuthenticationMessage" _authenticationMessage;
@"BKSWindowServerHitTestSecurityAnalysis" _securityAnalysis;
{CGPoint="x"d"y"d} _hitTestLocation;
{CGPoint="x"d"y"d} _preciseLocation;
```

## Properties

```
@property (Tq,N,V_pathIndex) pathIndex;
@property (TI,N,V_touchIdentifier) touchIdentifier;
@property (TI,N,V_userIdentifier) userIdentifier;
@property (TC,N,V_locus) locus;
@property (Tf,N,V_zGradient) zGradient;
@property (T{CGPoint=dd},N,V_hitTestLocation) hitTestLocation;
@property (T{CGPoint=dd},N,V_preciseLocation) preciseLocation;
@property (Tq,N,V_hitTestContextCategory) hitTestContextCategory;
@property (Td,D,N) hitTestLocationX;
@property (Td,D,N) hitTestLocationY;
@property (Td,D,N) preciseLocationX;
@property (Td,D,N) preciseLocationY;
@property (T@"<BKSHIDEventProvenance>",&,N) provenance;
@property (T@"BKSHIDEventDeferringChangeBasis",R,N) changeBasis;
@property (T@"BKSHIDEventAuthenticationMessage",&,N,V_authenticationMessage) authenticationMessage;
@property (T@"BKSWindowServerHitTestSecurityAnalysis",&,N,V_securityAnalysis) securityAnalysis;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDigitizerPathAttributes protobufSchema];
```

## Instance methods

```
-[BKSHIDEventDigitizerPathAttributes locus];
-[BKSHIDEventDigitizerPathAttributes userIdentifier];
-[BKSHIDEventDigitizerPathAttributes provenance];
-[BKSHIDEventDigitizerPathAttributes hitTestLocationX];
-[BKSHIDEventDigitizerPathAttributes authenticationMessage];
-[BKSHIDEventDigitizerPathAttributes hitTestContextCategory];
-[BKSHIDEventDigitizerPathAttributes touchIdentifier];
-[BKSHIDEventDigitizerPathAttributes preciseLocation];
-[BKSHIDEventDigitizerPathAttributes setPreciseLocationY:];
-[BKSHIDEventDigitizerPathAttributes setTouchIdentifier:];
-[BKSHIDEventDigitizerPathAttributes appendDescriptionToFormatter:];
-[BKSHIDEventDigitizerPathAttributes setZGradient:];
-[BKSHIDEventDigitizerPathAttributes setAuthenticationMessage:];
-[BKSHIDEventDigitizerPathAttributes setPathIndex:];
-[BKSHIDEventDigitizerPathAttributes zGradient];
-[BKSHIDEventDigitizerPathAttributes setHitTestLocationY:];
-[BKSHIDEventDigitizerPathAttributes setSecurityAnalysis:];
-[BKSHIDEventDigitizerPathAttributes hitTestLocationY];
-[BKSHIDEventDigitizerPathAttributes preciseLocationX];
-[BKSHIDEventDigitizerPathAttributes setPreciseLocationX:];
-[BKSHIDEventDigitizerPathAttributes securityAnalysis];
-[BKSHIDEventDigitizerPathAttributes setPreciseLocation:];
-[BKSHIDEventDigitizerPathAttributes setHitTestContextCategory:];
-[BKSHIDEventDigitizerPathAttributes description];
-[BKSHIDEventDigitizerPathAttributes setLocus:];
-[BKSHIDEventDigitizerPathAttributes preciseLocationY];
-[BKSHIDEventDigitizerPathAttributes setUserIdentifier:];
-[BKSHIDEventDigitizerPathAttributes copyWithZone:];
-[BKSHIDEventDigitizerPathAttributes setProvenance:];
-[BKSHIDEventDigitizerPathAttributes isEqual:];
-[BKSHIDEventDigitizerPathAttributes hitTestLocation];
-[BKSHIDEventDigitizerPathAttributes setHitTestLocation:];
-[BKSHIDEventDigitizerPathAttributes pathIndex];
-[BKSHIDEventDigitizerPathAttributes changeBasis];
-[BKSHIDEventDigitizerPathAttributes setHitTestLocationX:];
```
