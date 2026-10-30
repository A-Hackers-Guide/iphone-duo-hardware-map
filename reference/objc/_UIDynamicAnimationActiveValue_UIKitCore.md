# `_UIDynamicAnimationActiveValue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 4 properties, 17 instance methods, 3 class methods

## Instance variables

```
d _value;
d _minimumActiveValue;
d _maximumActiveValue;
i _type;
d _boundaryPull;
@ _applier;
b1 _lowerBoundary;
b1 _upperBoundary;
```

## Properties

```
@property (Td,N,V_value) value;
@property (Td,N,V_minimumActiveValue) minimumActiveValue;
@property (Td,N,V_maximumActiveValue) maximumActiveValue;
@property (Ti,N,V_type) type;
```

## Class methods

```
+[_UIDynamicAnimationActiveValue activeValue:ofType:];
+[_UIDynamicAnimationActiveValue lowerBoundary:ofType:];
+[_UIDynamicAnimationActiveValue upperBoundary:ofType:];
```

## Instance methods

```
-[_UIDynamicAnimationActiveValue init];
-[_UIDynamicAnimationActiveValue dealloc];
-[_UIDynamicAnimationActiveValue value];
-[_UIDynamicAnimationActiveValue setValue:];
-[_UIDynamicAnimationActiveValue setType:];
-[_UIDynamicAnimationActiveValue type];
-[_UIDynamicAnimationActiveValue description];
-[_UIDynamicAnimationActiveValue _appendDescriptionToString:atLevel:];
-[_UIDynamicAnimationActiveValue _applier];
-[_UIDynamicAnimationActiveValue _boundaryPull];
-[_UIDynamicAnimationActiveValue _isLowerBoundary];
-[_UIDynamicAnimationActiveValue _isUpperBoundary];
-[_UIDynamicAnimationActiveValue _setBoundaryPull:];
-[_UIDynamicAnimationActiveValue maximumActiveValue];
-[_UIDynamicAnimationActiveValue minimumActiveValue];
-[_UIDynamicAnimationActiveValue setMaximumActiveValue:];
-[_UIDynamicAnimationActiveValue setMinimumActiveValue:];
```
