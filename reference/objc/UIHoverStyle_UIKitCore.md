# `UIHoverStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 5 properties, 16 instance methods, 3 class methods

## Instance variables

```
_cachedBridgedEffect;
_effect;
_cachedBridgedShape;
_shape;
_isEnabled;
host;
driverCoordinator;
driverCoordinatorAccessLocked;
driverCoordinatorQueuedActions;
```

## Properties

```
@property (T@"NSString",N,R) verboseDescription;
@property (TB,N) enabled;
@property (T@"<UIHoverEffect>",N,&) effect;
@property (T@"UIShape",N,&) shape;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[UIHoverStyle automaticStyle];
+[UIHoverStyle styleWithShape:];
+[UIHoverStyle styleWithEffect:shape:];
```

## Instance methods

```
-[UIHoverStyle setShape:];
-[UIHoverStyle shape];
-[UIHoverStyle init];
-[UIHoverStyle effect];
-[UIHoverStyle isEnabled];
-[UIHoverStyle setEnabled:];
-[UIHoverStyle setEffect:];
-[UIHoverStyle description];
-[UIHoverStyle verboseDescription];
-[UIHoverStyle copyWithZone:];
-[UIHoverStyle isEqual:];
-[UIHoverStyle _invalidateAutomaticHoverEffect];
-[UIHoverStyle styleWithShape:];
-[UIHoverStyle _invalidateAutomaticHoverShape];
-[UIHoverStyle _invalidateCustomInteractionState];
-[UIHoverStyle styleWithEffect:shape:];
```
