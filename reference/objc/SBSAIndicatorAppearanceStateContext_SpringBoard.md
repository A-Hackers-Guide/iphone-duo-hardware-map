# `SBSAIndicatorAppearanceStateContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `NSCopying`, `SBSABlockMutating`
- 6 instance variables, 10 properties, 23 instance methods, 3 class methods

## Instance variables

```
@"SBSAIndicatorElementContext" _activeIndicatorElementContext;
q _interSensorIndicatorPhase;
q _microIndicatorPhase;
q _microIndicatorEjectionPhase;
q _renderedInterfaceOrientation;
Q _renderedLayoutDirection;
```

## Properties

```
@property (T@"SBSAIndicatorElementContext",&,N,S_setActiveIndicatorElementContext:,V_activeIndicatorElementContext) activeIndicatorElementContext;
@property (Tq,N,S_setInterSensorIndicatorPhase:,V_interSensorIndicatorPhase) interSensorIndicatorPhase;
@property (Tq,N,S_setMicroIndicatorPhase:,V_microIndicatorPhase) microIndicatorPhase;
@property (Tq,N,S_setMicroIndicatorEjectionPhase:,V_microIndicatorEjectionPhase) microIndicatorEjectionPhase;
@property (Tq,N,S_setRenderedInterfaceOrientation:,V_renderedInterfaceOrientation) renderedInterfaceOrientation;
@property (TQ,N,S_setRenderedLayoutDirection:,V_renderedLayoutDirection) renderedLayoutDirection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAIndicatorAppearanceStateContext initialize];
+[SBSAIndicatorAppearanceStateContext instanceWithBlock:];
+[SBSAIndicatorAppearanceStateContext mutatorClass];
```

## Instance methods

```
-[SBSAIndicatorAppearanceStateContext isSettled];
-[SBSAIndicatorAppearanceStateContext encodeWithCoder:];
-[SBSAIndicatorAppearanceStateContext hash];
-[SBSAIndicatorAppearanceStateContext description];
-[SBSAIndicatorAppearanceStateContext copyWithZone:];
-[SBSAIndicatorAppearanceStateContext isEqual:];
-[SBSAIndicatorAppearanceStateContext copyWithBlock:];
-[SBSAIndicatorAppearanceStateContext membersForCoder];
-[SBSAIndicatorAppearanceStateContext isDisappeared];
-[SBSAIndicatorAppearanceStateContext _isRenderedOrientationEqualToContext:];
-[SBSAIndicatorAppearanceStateContext _setActiveIndicatorElementContext:];
-[SBSAIndicatorAppearanceStateContext _setInterSensorIndicatorPhase:];
-[SBSAIndicatorAppearanceStateContext _setMicroIndicatorEjectionPhase:];
-[SBSAIndicatorAppearanceStateContext _setMicroIndicatorPhase:];
-[SBSAIndicatorAppearanceStateContext _setRenderedInterfaceOrientation:];
-[SBSAIndicatorAppearanceStateContext _setRenderedLayoutDirection:];
-[SBSAIndicatorAppearanceStateContext activeIndicatorElementContext];
-[SBSAIndicatorAppearanceStateContext interSensorIndicatorPhase];
-[SBSAIndicatorAppearanceStateContext isMicroVisible];
-[SBSAIndicatorAppearanceStateContext microIndicatorEjectionPhase];
-[SBSAIndicatorAppearanceStateContext microIndicatorPhase];
-[SBSAIndicatorAppearanceStateContext renderedInterfaceOrientation];
-[SBSAIndicatorAppearanceStateContext renderedLayoutDirection];
```
