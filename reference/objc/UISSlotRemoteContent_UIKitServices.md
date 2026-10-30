# `UISSlotRemoteContent`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `UISSlotAnyContent`
- 3 instance variables, 9 properties, 15 instance methods, 2 class methods

## Instance variables

```
C _contentScale;
{CGSize="width"d"height"d} _contentSize;
I _slotID;
```

## Properties

```
@property (TI,R,N,V_slotID) slotID;
@property (TC,R,N) contentScale;
@property (T{CGSize=dd},R,N) contentSize;
@property (TB,R,N) isRemote;
@property (TB,R,N) shouldReplaceExistingContent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISSlotRemoteContent supportsSecureCoding];
+[UISSlotRemoteContent newLayerContext];
```

## Instance methods

```
-[UISSlotRemoteContent isRemote];
-[UISSlotRemoteContent contentSize];
-[UISSlotRemoteContent encodeWithCoder:];
-[UISSlotRemoteContent contentScale];
-[UISSlotRemoteContent slotID];
-[UISSlotRemoteContent hash];
-[UISSlotRemoteContent initWithCoder:];
-[UISSlotRemoteContent image];
-[UISSlotRemoteContent isEqual:];
-[UISSlotRemoteContent deleteFromLayerContext:];
-[UISSlotRemoteContent initWithContentSize:contentScale:localImage:toLayerContext:];
-[UISSlotRemoteContent newTouchAuthenticationSpecificationWithAuthenticationMessageContext:backgroundStatisticsRegion:backgroundStatisticsForeground:backgroundStatisticsPassingContrast:backgroundStatisticsFailingContrast:hitTestInformationMask:initialSampleEvent:secureName:];
-[UISSlotRemoteContent shouldReplaceExistingContent];
-[UISSlotRemoteContent newTouchAuthenticationSpecificationWithAuthenticationMessageContext:backgroundStatisticsRegion:backgroundStatisticsForeground:backgroundStatisticsPassingContrast:backgroundStatisticsFailingContrast:hitTestInformationMask:initialSampleEvent:finalSampleEvent:longPressTimeout:secureName:];
-[UISSlotRemoteContent transferFromLayerContext:toLayerContextWithId:];
```
