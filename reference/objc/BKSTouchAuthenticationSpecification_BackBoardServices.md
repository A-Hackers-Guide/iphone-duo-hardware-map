# `BKSTouchAuthenticationSpecification`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`, `BSDescriptionStreamable`, `BSProtobufSerializable`
- 15 instance variables, 16 properties, 22 instance methods, 4 class methods

## Instance variables

```
@"NSSet" _displays;
I _slotID;
I _secureName;
Q _authenticationMessageContext;
S _backgroundStatisticsTopEdgeInset;
S _backgroundStatisticsLeftEdgeInset;
S _backgroundStatisticsBottomEdgeInset;
S _backgroundStatisticsRightEdgeInset;
f _backgroundStatisticsForeground;
f _backgroundStatisticsPassingContrast;
f _backgroundStatisticsFailingContrast;
Q _hitTestInformationMask;
q _initialSampleEvent;
q _finalSampleEvent;
d _longPressTimeout;
```

## Properties

```
@property (T@"NSSet",R,C,N,V_displays) displays;
@property (TI,R,N,V_slotID) slotID;
@property (TQ,R,N,V_authenticationMessageContext) authenticationMessageContext;
@property (TI,R,N,V_secureName) secureName;
@property (T{?=SSSS},R,N) backgroundStatisticsRegion;
@property (Tf,R,N,V_backgroundStatisticsForeground) backgroundStatisticsForeground;
@property (Tf,R,N,V_backgroundStatisticsPassingContrast) backgroundStatisticsPassingContrast;
@property (Tf,R,N,V_backgroundStatisticsFailingContrast) backgroundStatisticsFailingContrast;
@property (TQ,R,N,V_hitTestInformationMask) hitTestInformationMask;
@property (Tq,R,N,V_initialSampleEvent) initialSampleEvent;
@property (Tq,R,N,V_finalSampleEvent) finalSampleEvent;
@property (Td,R,N,V_longPressTimeout) longPressTimeout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSTouchAuthenticationSpecification supportsSecureCoding];
+[BKSTouchAuthenticationSpecification protobufSchema];
+[BKSTouchAuthenticationSpecification new];
+[BKSTouchAuthenticationSpecification buildSpecification:];
```

## Instance methods

```
-[BKSTouchAuthenticationSpecification mutableCopyWithZone:];
-[BKSTouchAuthenticationSpecification backgroundStatisticsFailingContrast];
-[BKSTouchAuthenticationSpecification initForProtobufDecoding];
-[BKSTouchAuthenticationSpecification hitTestInformationMask];
-[BKSTouchAuthenticationSpecification init];
-[BKSTouchAuthenticationSpecification initialSampleEvent];
-[BKSTouchAuthenticationSpecification appendDescriptionToFormatter:];
-[BKSTouchAuthenticationSpecification authenticationMessageContext];
-[BKSTouchAuthenticationSpecification displays];
-[BKSTouchAuthenticationSpecification backgroundStatisticsForeground];
-[BKSTouchAuthenticationSpecification backgroundStatisticsPassingContrast];
-[BKSTouchAuthenticationSpecification secureName];
-[BKSTouchAuthenticationSpecification encodeWithCoder:];
-[BKSTouchAuthenticationSpecification slotID];
-[BKSTouchAuthenticationSpecification backgroundStatisticsRegion];
-[BKSTouchAuthenticationSpecification hash];
-[BKSTouchAuthenticationSpecification description];
-[BKSTouchAuthenticationSpecification initWithCoder:];
-[BKSTouchAuthenticationSpecification copyWithZone:];
-[BKSTouchAuthenticationSpecification isEqual:];
-[BKSTouchAuthenticationSpecification longPressTimeout];
-[BKSTouchAuthenticationSpecification finalSampleEvent];
```
