# `BLSBacklightChangeEvent`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSSecureCoding`, `BLSDisplaySpecifying`
- 8 instance variables, 12 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _transitioning;
B _transitionForcedUnanimated;
B _environmentTransitionAnimated;
@"<BLSDisplay>" _display;
Q _eventID;
q _state;
q _previousState;
@"BLSBacklightChangeRequest" _changeRequest;
```

## Properties

```
@property (TB,R,N,GisTransitionForcedUnanimated,V_transitionForcedUnanimated) transitionForcedUnanimated;
@property (TB,R,N,GisEnvironmentTransitionAnimated,V_environmentTransitionAnimated) environmentTransitionAnimated;
@property (TQ,R,N,V_eventID) eventID;
@property (Tq,R,N,V_state) state;
@property (Tq,R,N,V_previousState) previousState;
@property (TB,R,N,GwasTransitioning,V_transitioning) transitioning;
@property (T@"BLSBacklightChangeRequest",R,N,V_changeRequest) changeRequest;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BLSDisplay>",R,N,V_display) display;
```

## Class methods

```
+[BLSBacklightChangeEvent supportsSecureCoding];
```

## Instance methods

```
-[BLSBacklightChangeEvent bls_loggingString];
-[BLSBacklightChangeEvent display];
-[BLSBacklightChangeEvent bls_shortLoggingString];
-[BLSBacklightChangeEvent eventID];
-[BLSBacklightChangeEvent changeRequest];
-[BLSBacklightChangeEvent initWithXPCDictionary:];
-[BLSBacklightChangeEvent previousState];
-[BLSBacklightChangeEvent encodeWithXPCDictionary:];
-[BLSBacklightChangeEvent encodeWithCoder:];
-[BLSBacklightChangeEvent hash];
-[BLSBacklightChangeEvent description];
-[BLSBacklightChangeEvent initWithCoder:];
-[BLSBacklightChangeEvent copyWithZone:];
-[BLSBacklightChangeEvent isEqual:];
-[BLSBacklightChangeEvent state];
-[BLSBacklightChangeEvent isEnvironmentTransitionAnimated];
-[BLSBacklightChangeEvent initWithEventID:state:previousState:changeRequest:];
-[BLSBacklightChangeEvent initWithEventID:state:previousState:wasTransitioning:changeRequest:display:];
-[BLSBacklightChangeEvent isTransitionForcedUnanimated];
-[BLSBacklightChangeEvent setTransitionForcedUnanimated:environmentTransitionAnimated:];
-[BLSBacklightChangeEvent wasTransitioning];
-[BLSBacklightChangeEvent initWithEventID:state:previousState:wasTransitioning:changeRequest:];
```
