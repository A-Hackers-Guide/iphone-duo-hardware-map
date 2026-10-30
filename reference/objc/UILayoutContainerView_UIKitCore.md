# `UILayoutContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIAssertionControllerSubject`, `NSCoding`
- 7 instance variables, 9 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"UIView" _shadowView;
@"_UIAssertionController" _assertionController;
{?="delegateRespondsToSemanticContentAttributeChanged"b1"delegateRespondsToViewWillLayoutSubviews"b1"delegateRespondsToWillMoveToWindow"b1"delegateRespondsToDidMoveToWindow"b1"backgroundColorIsDefault"b1"disableUserInteraction"b1} _layoutContainerViewFlags;
B _usesInnerShadow;
B _usesRoundedCorners;
@"<UILayoutContainerViewDelegate>" _delegate;
@"UIColor" _defaultBackgroundColor;
```

## Properties

```
@property (T@"<UILayoutContainerViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_usesInnerShadow) usesInnerShadow;
@property (TB,N,V_usesRoundedCorners) usesRoundedCorners;
@property (T@"UIColor",&,N,V_defaultBackgroundColor) defaultBackgroundColor;
@property (TB,R,N) backgroundColorIsDefault;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UILayoutContainerView _commonInit];
-[UILayoutContainerView assertionActivationStateForType:];
-[UILayoutContainerView didMoveToWindow];
-[UILayoutContainerView _setFlagsFromDelegate:];
-[UILayoutContainerView _systemDefaultFocusGroupIdentifier];
-[UILayoutContainerView _updateShadowViews];
-[UILayoutContainerView addSubview:];
-[UILayoutContainerView _disableUserInteractionForReason:];
-[UILayoutContainerView usesInnerShadow];
-[UILayoutContainerView setUsesRoundedCorners:];
-[UILayoutContainerView setDefaultBackgroundColor:];
-[UILayoutContainerView defaultBackgroundColor];
-[UILayoutContainerView dealloc];
-[UILayoutContainerView backgroundColorIsDefault];
-[UILayoutContainerView layoutSubviews];
-[UILayoutContainerView hitTest:withEvent:];
-[UILayoutContainerView setBounds:];
-[UILayoutContainerView setSemanticContentAttribute:];
-[UILayoutContainerView setBackgroundColor:];
-[UILayoutContainerView setDelegate:];
-[UILayoutContainerView willMoveToWindow:];
-[UILayoutContainerView _installShadowViews];
-[UILayoutContainerView usesRoundedCorners];
-[UILayoutContainerView encodeWithCoder:];
-[UILayoutContainerView setUsesInnerShadow:];
-[UILayoutContainerView _tearDownShadowViews];
-[UILayoutContainerView delegate];
-[UILayoutContainerView setFrame:];
-[UILayoutContainerView assertionActivationStateChangedToState:forType:];
-[UILayoutContainerView initWithCoder:];
-[UILayoutContainerView initWithFrame:];
```
