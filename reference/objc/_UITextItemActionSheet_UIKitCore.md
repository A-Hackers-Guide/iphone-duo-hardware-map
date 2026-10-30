# `_UITextItemActionSheet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIRotatingAlertControllerDelegate`
- 6 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSString" _title;
@"UIView" _view;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
@"NSArray" _ddActions;
@"_UIRotatingAlertController" _alertController;
@"UIWindow" _alertWindow;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextItemActionSheet present];
-[_UITextItemActionSheet dealloc];
-[_UITextItemActionSheet _alertActionsWithController:];
-[_UITextItemActionSheet _hasAlertActions];
-[_UITextItemActionSheet hostViewForSheet:];
-[_UITextItemActionSheet initWithTitle:dataDetectorActions:fromRect:inView:];
-[_UITextItemActionSheet initialPresentationRectInHostViewForSheet:];
-[_UITextItemActionSheet presentationRectInHostViewForSheet:];
```
