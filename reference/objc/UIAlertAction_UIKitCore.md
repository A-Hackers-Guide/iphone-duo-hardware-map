# `UIAlertAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 19 instance variables, 15 properties, 43 instance methods, 5 class methods

## Instance variables

```
@"NSString" _title;
q _titleTextAlignment;
B _enabled;
B _checked;
B _isPreferred;
@"UIColor" _imageTintColor;
@"UIColor" _titleTextColor;
q _style;
@? _handler;
@? _simpleHandler;
@"UIImage" _image;
@? _shouldDismissHandler;
@"NSString" __descriptiveText;
@"UIViewController" _contentViewController;
@"NSString" _keyCommandInput;
q _keyCommandModifierFlags;
@"UIInterfaceAction<_UIAlertActionMutablePropertyObservering>" __interfaceActionRepresentation;
@"UIAlertController" __alertController;
@"<_UIAlertActionViewRepresentation>" __representer;
```

## Properties

```
@property (T@?,C,N,V_handler) handler;
@property (Tq,N,V_style) style;
@property (T@?,C,N,V_simpleHandler) simpleHandler;
@property (T@"UIImage",&,N,V_image) image;
@property (T@?,C,N,V_shouldDismissHandler) shouldDismissHandler;
@property (T@"NSString",C,N,S_setDescriptiveText:,V__descriptiveText) _descriptiveText;
@property (T@"UIViewController",&,N,G_contentViewController,S_setContentViewController:,V_contentViewController) contentViewController;
@property (T@"NSString",C,N,G_keyCommandInput,S_setKeyCommandInput:,V_keyCommandInput) keyCommandInput;
@property (Tq,N,G_keyCommandModifierFlags,S_setKeyCommandModifierFlags:,V_keyCommandModifierFlags) keyCommandModifierFlags;
@property (T@"UIInterfaceAction<_UIAlertActionMutablePropertyObservering>",S_setInterfaceActionRepresentation:,V__interfaceActionRepresentation) _interfaceActionRepresentation;
@property (TB,S_setIsPreferred:) _isPreferred;
@property (T@"UIAlertController",N,S_setAlertController:,V__alertController) _alertController;
@property (T@"<_UIAlertActionViewRepresentation>",S_setRepresenter:,V__representer) _representer;
@property (T@"NSString",C,N,V_title) title;
@property (TB,N,GisEnabled) enabled;
```

## Class methods

```
+[UIAlertAction _actionWithContentViewController:style:];
+[UIAlertAction _actionWithContentViewController:style:handler:];
+[UIAlertAction _actionWithTitle:descriptiveText:image:style:handler:shouldDismissHandler:];
+[UIAlertAction _actionWithTitle:image:style:handler:shouldDismissHandler:];
+[UIAlertAction actionWithTitle:style:handler:];
```

## Instance methods

```
-[UIAlertAction _setContentViewController:];
-[UIAlertAction _descriptiveText];
-[UIAlertAction simpleHandler];
-[UIAlertAction _setTitleTextAlignment:];
-[UIAlertAction _didAddContentViewController];
-[UIAlertAction setShouldDismissHandler:];
-[UIAlertAction _setAlertController:];
-[UIAlertAction setHandler:];
-[UIAlertAction _contentViewController];
-[UIAlertAction setSimpleHandler:];
-[UIAlertAction style];
-[UIAlertAction _setImageTintColor:];
-[UIAlertAction setStyle:];
-[UIAlertAction _setKeyCommandModifierFlags:];
-[UIAlertAction isEnabled];
-[UIAlertAction _representer];
-[UIAlertAction _titleTextColor];
-[UIAlertAction _willAddContentViewController];
-[UIAlertAction _setKeyCommandInput:];
-[UIAlertAction title];
-[UIAlertAction _titleTextAlignment];
-[UIAlertAction setEnabled:];
-[UIAlertAction handler];
-[UIAlertAction _isChecked];
-[UIAlertAction description];
-[UIAlertAction setTitle:];
-[UIAlertAction _setChecked:];
-[UIAlertAction _keyCommandModifierFlags];
-[UIAlertAction _setIsPreferred:];
-[UIAlertAction image];
-[UIAlertAction _alertController];
-[UIAlertAction copyWithZone:];
-[UIAlertAction _isPreferred];
-[UIAlertAction _setRepresenter:];
-[UIAlertAction _keyCommandInput];
-[UIAlertAction _setInterfaceActionRepresentation:];
-[UIAlertAction _setDescriptiveText:];
-[UIAlertAction shouldDismissHandler];
-[UIAlertAction _setTitleTextColor:];
-[UIAlertAction _setKeyCommandInput:modifierFlags:];
-[UIAlertAction _imageTintColor];
-[UIAlertAction _interfaceActionRepresentation];
-[UIAlertAction setImage:];
```
