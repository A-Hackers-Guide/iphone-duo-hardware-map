# `_UIViewPropertyAnimationUpdate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _additive;
B _implicit;
@"NSString" _propertyName;
@"NSValue" _fromValue;
@"NSValue" _toValue;
d _startTime;
d _duration;
d _delay;
```

## Properties

```
@property (TB,R,N,GisImplicit,V_implicit) implicit;
@property (T@"NSString",R,N,V_propertyName) propertyName;
@property (TB,R,N,GisAdditive,V_additive) additive;
@property (T@"NSValue",&,N,V_fromValue) fromValue;
@property (T@"NSValue",&,N,V_toValue) toValue;
@property (Td,N,V_startTime) startTime;
@property (Td,N,V_duration) duration;
@property (Td,N,V_delay) delay;
```

## Instance methods

```
-[_UIViewPropertyAnimationUpdate isAdditive];
-[_UIViewPropertyAnimationUpdate init];
-[_UIViewPropertyAnimationUpdate startTime];
-[_UIViewPropertyAnimationUpdate propertyName];
-[_UIViewPropertyAnimationUpdate duration];
-[_UIViewPropertyAnimationUpdate delay];
-[_UIViewPropertyAnimationUpdate setStartTime:];
-[_UIViewPropertyAnimationUpdate setDelay:];
-[_UIViewPropertyAnimationUpdate isImplicit];
-[_UIViewPropertyAnimationUpdate setDuration:];
-[_UIViewPropertyAnimationUpdate toValue];
-[_UIViewPropertyAnimationUpdate fromValue];
-[_UIViewPropertyAnimationUpdate setFromValue:];
-[_UIViewPropertyAnimationUpdate setToValue:];
-[_UIViewPropertyAnimationUpdate initWithPropertyName:implicit:additive:];
```
