# `_UIInterfaceActionImagePropertyView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIImageView`
- Protocols: `UIInterfaceActionDisplayPropertyObserver`
- 4 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSLayoutConstraint" _imageWidthConstraint;
@"NSLayoutConstraint" _imageHeightConstraint;
@"UIInterfaceAction" _action;
@"NSString" _imageProperty;
```

## Properties

```
@property (T@"UIInterfaceAction",R,N,V_action) action;
@property (T@"NSString",R,N,V_imageProperty) imageProperty;
@property (TB,R,N) isUsedToOccupySpaceIfNoImage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIInterfaceActionImagePropertyView dealloc];
-[_UIInterfaceActionImagePropertyView action];
-[_UIInterfaceActionImagePropertyView _visualStyle];
-[_UIInterfaceActionImagePropertyView tintColorDidChange];
-[_UIInterfaceActionImagePropertyView _applyVisualStyle];
-[_UIInterfaceActionImagePropertyView interfaceAction:reloadDisplayedContentVisualStyle:];
-[_UIInterfaceActionImagePropertyView interfaceAction:reloadDisplayedContentActionProperties:];
-[_UIInterfaceActionImagePropertyView setImage:];
-[_UIInterfaceActionImagePropertyView _applyVisualStyleToImageView];
-[_UIInterfaceActionImagePropertyView _interfaceActionViewState];
-[_UIInterfaceActionImagePropertyView _reloadImageContent];
-[_UIInterfaceActionImagePropertyView _sizeToOccupy];
-[_UIInterfaceActionImagePropertyView imageProperty];
-[_UIInterfaceActionImagePropertyView initWithAction:imageProperty:];
-[_UIInterfaceActionImagePropertyView isUsedToOccupySpaceIfNoImage];
```
