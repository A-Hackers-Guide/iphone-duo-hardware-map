# `_UIAlertControllerActionViewInterfaceAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInterfaceAction`
- Protocols: `_UIAlertActionMutablePropertyObservering`
- 2 instance variables, 7 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"UIAlertAction" _underlyingAlertAction;
B _valid;
```

## Properties

```
@property (T@"_UIAlertControllerActionView",R,D,N) alertControllerActionView;
@property (T@"UIAlertAction",R,N,V_underlyingAlertAction) underlyingAlertAction;
@property (TB,R,N,V_valid) valid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIAlertControllerActionViewInterfaceAction actionWithAlertControllerActionView:];
```

## Instance methods

```
-[_UIAlertControllerActionViewInterfaceAction valid];
-[_UIAlertControllerActionViewInterfaceAction leadingImage];
-[_UIAlertControllerActionViewInterfaceAction _initializeStateFromUnderlyingAlertAction];
-[_UIAlertControllerActionViewInterfaceAction dealloc];
-[_UIAlertControllerActionViewInterfaceAction _action:changedToChecked:];
-[_UIAlertControllerActionViewInterfaceAction classificationTitle];
-[_UIAlertControllerActionViewInterfaceAction _action:changedToBePreferred:];
-[_UIAlertControllerActionViewInterfaceAction invalidate];
-[_UIAlertControllerActionViewInterfaceAction type];
-[_UIAlertControllerActionViewInterfaceAction _action:changedToTitle:];
-[_UIAlertControllerActionViewInterfaceAction underlyingAlertAction];
-[_UIAlertControllerActionViewInterfaceAction alertControllerActionView];
-[_UIAlertControllerActionViewInterfaceAction _typeForDeterminingViewRepresentation];
-[_UIAlertControllerActionViewInterfaceAction _action:changedToTitleTextAlignment:];
-[_UIAlertControllerActionViewInterfaceAction _action:updatedTitleTextColor:];
-[_UIAlertControllerActionViewInterfaceAction _action:updatedImageTintColor:];
-[_UIAlertControllerActionViewInterfaceAction _action:changedToEnabled:];
```
