# `BKTouchPadInfo`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
I _pathIndexInRangeMask;
I _pathIndexTouchingMask;
f _maxForce;
@"<BKHIDEventSenderInfo>" _senderInfo;
@"BKSHIDEventSenderDescriptor" _overrideSenderDescriptor;
@"<BKHIDEventDispatcher>" _eventDispatcher;
@"NSSet" _currentDestinations;
{CGSize="width"d"height"d} _digitizerSurfaceDimensions;
```

## Properties

```
@property (T@"<BKHIDEventSenderInfo>",&,N,V_senderInfo) senderInfo;
@property (T@"BKSHIDEventSenderDescriptor",&,N,V_overrideSenderDescriptor) overrideSenderDescriptor;
@property (T@"<BKHIDEventDispatcher>",&,N,V_eventDispatcher) eventDispatcher;
@property (T@"NSSet",&,N,V_currentDestinations) currentDestinations;
@property (TI,N,V_pathIndexInRangeMask) pathIndexInRangeMask;
@property (TI,N,V_pathIndexTouchingMask) pathIndexTouchingMask;
@property (Tf,N,V_maxForce) maxForce;
@property (T{CGSize=dd},N,V_digitizerSurfaceDimensions) digitizerSurfaceDimensions;
```

## Instance methods

```
-[BKTouchPadInfo eventDispatcher];
-[BKTouchPadInfo setEventDispatcher:];
-[BKTouchPadInfo maxForce];
-[BKTouchPadInfo description];
-[BKTouchPadInfo initWithService:];
-[BKTouchPadInfo senderInfo];
-[BKTouchPadInfo setSenderInfo:];
-[BKTouchPadInfo currentDestinations];
-[BKTouchPadInfo digitizerSurfaceDimensions];
-[BKTouchPadInfo overrideSenderDescriptor];
-[BKTouchPadInfo pathIndexInRangeMask];
-[BKTouchPadInfo pathIndexTouchingMask];
-[BKTouchPadInfo resetForCancel];
-[BKTouchPadInfo setCurrentDestinations:];
-[BKTouchPadInfo setDigitizerSurfaceDimensions:];
-[BKTouchPadInfo setMaxForce:];
-[BKTouchPadInfo setOverrideSenderDescriptor:];
-[BKTouchPadInfo setPathIndexInRangeMask:];
-[BKTouchPadInfo setPathIndexTouchingMask:];
```
