# `UIPointerRegionRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _modifiers;
q __pointerType;
{CGPoint="x"d"y"d} _location;
```

## Properties

```
@property (T{CGPoint=dd},N,V_location) location;
@property (Tq,N,V_modifiers) modifiers;
@property (Tq,N,V__pointerType) _pointerType;
```

## Instance methods

```
-[UIPointerRegionRequest location];
-[UIPointerRegionRequest setLocation:];
-[UIPointerRegionRequest description];
-[UIPointerRegionRequest _isPencilInitiated];
-[UIPointerRegionRequest _pointerType];
-[UIPointerRegionRequest modifiers];
-[UIPointerRegionRequest setModifiers:];
-[UIPointerRegionRequest set_pointerType:];
```
