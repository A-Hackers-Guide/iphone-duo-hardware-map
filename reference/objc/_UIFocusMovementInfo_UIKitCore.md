# `_UIFocusMovementInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSXPCCoding`
- 10 instance variables, 14 properties, 27 instance methods, 2 class methods

## Instance variables

```
B _looping;
B _shouldLoadScrollableContainer;
B _isVelocityBased;
B _isInitialMovement;
Q _heading;
Q _linearHeading;
q _groupFilter;
Q _inputType;
{CGVector="dx"d"dy"d} _velocity;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _fallbackMovementOriginatingFrame;
```

## Properties

```
@property (TQ,N,S_setHeading:,V_heading) heading;
@property (TB,N,G_isLooping,S_setLooping:,V_looping) looping;
@property (TQ,N,G_linearHeading,S_setLinearHeading:,V_linearHeading) linearHeading;
@property (TB,N,G_shouldLoadScrollableContainer,S_setShouldLoadScrollableContainer:,V_shouldLoadScrollableContainer) shouldLoadScrollableContainer;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,G_fallbackMovementOriginatingFrame,S_setFallbackMovementOriginatingFrame:,V_fallbackMovementOriginatingFrame) fallbackMovementOriginatingFrame;
@property (Tq,N,G_groupFilter,S_setGroupFilter:,V_groupFilter) groupFilter;
@property (TQ,R,N,G_inputType,V_inputType) inputType;
@property (TB,R,N,G_isVelocityBased,V_isVelocityBased) isVelocityBased;
@property (T{CGVector=dd},R,N,G_velocity,V_velocity) velocity;
@property (TB,R,N,G_isInitialMovement,V_isInitialMovement) isInitialMovement;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIFocusMovementInfo supportsSecureCoding];
+[_UIFocusMovementInfo _movementWithHeading:isInitial:fallbackMovementOriginatingFrame:];
```

## Instance methods

```
-[_UIFocusMovementInfo _velocity];
-[_UIFocusMovementInfo init];
-[_UIFocusMovementInfo initWithXPCDictionary:];
-[_UIFocusMovementInfo heading];
-[_UIFocusMovementInfo encodeWithXPCDictionary:];
-[_UIFocusMovementInfo encodeWithCoder:];
-[_UIFocusMovementInfo description];
-[_UIFocusMovementInfo initWithCoder:];
-[_UIFocusMovementInfo copyWithZone:];
-[_UIFocusMovementInfo _fallbackMovementOriginatingFrame];
-[_UIFocusMovementInfo _groupFilter];
-[_UIFocusMovementInfo _inputType];
-[_UIFocusMovementInfo _isInitialMovement];
-[_UIFocusMovementInfo _isLinearMovement];
-[_UIFocusMovementInfo _isLooping];
-[_UIFocusMovementInfo _isVelocityBased];
-[_UIFocusMovementInfo _linearHeading];
-[_UIFocusMovementInfo _setFallbackMovementOriginatingFrame:];
-[_UIFocusMovementInfo _setGroupFilter:];
-[_UIFocusMovementInfo _setHeading:];
-[_UIFocusMovementInfo _setLinearHeading:];
-[_UIFocusMovementInfo _setLooping:];
-[_UIFocusMovementInfo _setShouldLoadScrollableContainer:];
-[_UIFocusMovementInfo _shouldLoadScrollableContainer];
-[_UIFocusMovementInfo initWithHeading:linearHeading:isInitial:shouldLoadScrollableContainer:looping:groupFilter:];
-[_UIFocusMovementInfo initWithHeading:linearHeading:isInitial:shouldLoadScrollableContainer:looping:groupFilter:inputType:];
-[_UIFocusMovementInfo initWithHeading:velocity:isInitial:shouldLoadScrollableContainer:groupFilter:inputType:];
```
