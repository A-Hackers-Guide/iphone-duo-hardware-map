# `UIAlertControllerDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 11 instance variables, 11 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _hasHeaderContentViewController;
B _hasTitle;
B _hasMessage;
B _hasContentViewController;
B _applicationIsFullscreen;
B _hasTextfields;
B _isPad;
B _isSystemAlert;
q _numberOfActions;
q _numberOfVisibleActions;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _containerViewSafeAreaInsets;
```

## Properties

```
@property (TB,V_hasHeaderContentViewController) hasHeaderContentViewController;
@property (TB,V_hasTitle) hasTitle;
@property (TB,V_hasMessage) hasMessage;
@property (TB,V_hasContentViewController) hasContentViewController;
@property (Tq,V_numberOfActions) numberOfActions;
@property (Tq,V_numberOfVisibleActions) numberOfVisibleActions;
@property (TB,V_applicationIsFullscreen) applicationIsFullscreen;
@property (T{UIEdgeInsets=dddd},V_containerViewSafeAreaInsets) containerViewSafeAreaInsets;
@property (TB,V_hasTextfields) hasTextfields;
@property (TB,V_isPad) isPad;
@property (TB,V_isSystemAlert) isSystemAlert;
```

## Instance methods

```
-[UIAlertControllerDescriptor isPad];
-[UIAlertControllerDescriptor setIsPad:];
-[UIAlertControllerDescriptor setHasTitle:];
-[UIAlertControllerDescriptor setNumberOfActions:];
-[UIAlertControllerDescriptor numberOfActions];
-[UIAlertControllerDescriptor numberOfVisibleActions];
-[UIAlertControllerDescriptor setNumberOfVisibleActions:];
-[UIAlertControllerDescriptor hasMessage];
-[UIAlertControllerDescriptor setHasHeaderContentViewController:];
-[UIAlertControllerDescriptor hasTextfields];
-[UIAlertControllerDescriptor setApplicationIsFullscreen:];
-[UIAlertControllerDescriptor applicationIsFullscreen];
-[UIAlertControllerDescriptor setHasMessage:];
-[UIAlertControllerDescriptor setIsSystemAlert:];
-[UIAlertControllerDescriptor setContainerViewSafeAreaInsets:];
-[UIAlertControllerDescriptor isSystemAlert];
-[UIAlertControllerDescriptor hasContentViewController];
-[UIAlertControllerDescriptor copyWithZone:];
-[UIAlertControllerDescriptor containerViewSafeAreaInsets];
-[UIAlertControllerDescriptor isEqual:];
-[UIAlertControllerDescriptor setHasTextfields:];
-[UIAlertControllerDescriptor hasHeaderContentViewController];
-[UIAlertControllerDescriptor hasTitle];
-[UIAlertControllerDescriptor setHasContentViewController:];
```
