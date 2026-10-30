# `UIInterfaceAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 20 instance variables, 21 properties, 48 instance methods, 6 class methods

## Instance variables

```
B _enabled;
B _preferred;
B _focused;
@"UIView" _customContentView;
q _type;
@"UIViewController" _customContentViewController;
@"NSString" _title;
q _titleAlignment;
@"NSString" _classificationTitle;
@"UIImage" _leadingImage;
@"UIImage" _trailingImage;
@? _handler;
@"NSPointerArray" _weakDisplayPropertyObservers;
@"UIInterfaceActionRepresentationView" __visualRepresentation;
@"<_UIInterfaceActionPresenting>" __presentingController;
@"UIInterfaceActionVisualStyle" _visualStyle;
@"UIColor" _titleTextColor;
@"UIColor" _imageTintColor;
{CGSize="width"d"height"d} _leadingImageLayoutSize;
{CGSize="width"d"height"d} _trailingImageLayoutSize;
```

## Properties

```
@property (T@"UIViewController",&,N,V_customContentViewController) customContentViewController;
@property (T@?,C,N,V_handler) handler;
@property (Tq,N,V_type) type;
@property (T@"NSPointerArray",R,N,V_weakDisplayPropertyObservers) weakDisplayPropertyObservers;
@property (Tq,R,N) _typeForDeterminingViewRepresentation;
@property (T@"UIView",R,N,V_customContentView) customContentView;
@property (T@"UIInterfaceActionRepresentationView",W,N,S_setVisualRepresentation:,V__visualRepresentation) _visualRepresentation;
@property (T@"<_UIInterfaceActionPresenting>",W,N,S_setPresentingController:,V__presentingController) _presentingController;
@property (T{CGSize=dd},N,V_leadingImageLayoutSize) leadingImageLayoutSize;
@property (T{CGSize=dd},N,V_trailingImageLayoutSize) trailingImageLayoutSize;
@property (TB,N,G_isPreferred,S_setIsPreferred:,V_preferred) preferred;
@property (TB,N,G_isFocused,S_setIsFocused:,V_focused) focused;
@property (T@"UIInterfaceActionVisualStyle",&,N,G_visualStyle,S_setVisualStyle:,V_visualStyle) visualStyle;
@property (T@"UIColor",&,N,G_titleTextColor,S_setTitleTextColor:,V_titleTextColor) titleTextColor;
@property (T@"UIColor",&,N,G_imageTintColor,S_setImageTintColor:,V_imageTintColor) imageTintColor;
@property (T@"NSString",C,N,V_title) title;
@property (Tq,N,V_titleAlignment) titleAlignment;
@property (T@"NSString",C,N,V_classificationTitle) classificationTitle;
@property (T@"UIImage",&,N,V_leadingImage) leadingImage;
@property (T@"UIImage",&,N,V_trailingImage) trailingImage;
@property (TB,N,GisEnabled,V_enabled) enabled;
```

## Class methods

```
+[UIInterfaceAction _setInterfaceActionCanInvokeActionsWithoutPresentingController:];
+[UIInterfaceAction _observableDisplayProperties];
+[UIInterfaceAction actionWithCustomContentView:handler:];
+[UIInterfaceAction actionWithCustomContentViewController:];
+[UIInterfaceAction actionWithTitle:type:handler:];
+[UIInterfaceAction changedProperties:containsAny:];
```

## Instance methods

```
-[UIInterfaceAction customContentView];
-[UIInterfaceAction setTitleAlignment:];
-[UIInterfaceAction leadingImage];
-[UIInterfaceAction titleAlignment];
-[UIInterfaceAction setLeadingImageLayoutSize:];
-[UIInterfaceAction _notifyObserversVisualStyleDidChange];
-[UIInterfaceAction setHandler:];
-[UIInterfaceAction classificationTitle];
-[UIInterfaceAction _visualStyle];
-[UIInterfaceAction _setImageTintColor:];
-[UIInterfaceAction isEnabled];
-[UIInterfaceAction setTrailingImageLayoutSize:];
-[UIInterfaceAction _titleTextColor];
-[UIInterfaceAction setLeadingImage:];
-[UIInterfaceAction setType:];
-[UIInterfaceAction type];
-[UIInterfaceAction title];
-[UIInterfaceAction setEnabled:];
-[UIInterfaceAction handler];
-[UIInterfaceAction _setVisualStyle:];
-[UIInterfaceAction _notifyObserversDidChangeActionProperty:];
-[UIInterfaceAction description];
-[UIInterfaceAction trailingImageLayoutSize];
-[UIInterfaceAction _typeForDeterminingViewRepresentation];
-[UIInterfaceAction setTitle:];
-[UIInterfaceAction _setIsPreferred:];
-[UIInterfaceAction copyWithZone:];
-[UIInterfaceAction _isPreferred];
-[UIInterfaceAction weakDisplayPropertyObservers];
-[UIInterfaceAction _setTitleTextColor:];
-[UIInterfaceAction _imageTintColor];
-[UIInterfaceAction leadingImageLayoutSize];
-[UIInterfaceAction setCustomContentViewController:];
-[UIInterfaceAction _addActionDisplayPropertyObserver:];
-[UIInterfaceAction _invokeHandlerWithCompletionBlock:];
-[UIInterfaceAction _isFocused];
-[UIInterfaceAction _layoutSizeForImageProperty:];
-[UIInterfaceAction _presentingController];
-[UIInterfaceAction _removeActionDisplayPropertyObserver:];
-[UIInterfaceAction _setIsFocused:];
-[UIInterfaceAction _setPresentingController:];
-[UIInterfaceAction _setVisualRepresentation:];
-[UIInterfaceAction _visualRepresentation];
-[UIInterfaceAction customContentViewController];
-[UIInterfaceAction initWithTitle:type:customContentViewController:customContentView:handler:];
-[UIInterfaceAction setClassificationTitle:];
-[UIInterfaceAction setTrailingImage:];
-[UIInterfaceAction trailingImage];
```
