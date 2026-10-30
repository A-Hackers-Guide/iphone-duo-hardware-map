# `LAPSPasscodeOptionsPresentationRequest`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _animated;
@"UIViewController" _sourceViewController;
@"UIView" _sourceView;
@"UIBarButtonItem" _sourceItem;
@"LACUIPasscodeServiceOptionsViewConfiguration" _config;
q _presentationStyle;
@"<LAPSPasscodeOptionsViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"UIViewController",R,N,V_sourceViewController) sourceViewController;
@property (T@"UIView",&,N,V_sourceView) sourceView;
@property (T@"UIBarButtonItem",&,N,V_sourceItem) sourceItem;
@property (T@"LACUIPasscodeServiceOptionsViewConfiguration",&,N,V_config) config;
@property (TB,N,V_animated) animated;
@property (Tq,N,V_presentationStyle) presentationStyle;
@property (T@"<LAPSPasscodeOptionsViewControllerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[LAPSPasscodeOptionsPresentationRequest config];
-[LAPSPasscodeOptionsPresentationRequest setConfig:];
-[LAPSPasscodeOptionsPresentationRequest setPresentationStyle:];
-[LAPSPasscodeOptionsPresentationRequest animated];
-[LAPSPasscodeOptionsPresentationRequest presentationStyle];
-[LAPSPasscodeOptionsPresentationRequest setAnimated:];
-[LAPSPasscodeOptionsPresentationRequest setDelegate:];
-[LAPSPasscodeOptionsPresentationRequest setSourceView:];
-[LAPSPasscodeOptionsPresentationRequest delegate];
-[LAPSPasscodeOptionsPresentationRequest setSourceItem:];
-[LAPSPasscodeOptionsPresentationRequest sourceView];
-[LAPSPasscodeOptionsPresentationRequest sourceItem];
-[LAPSPasscodeOptionsPresentationRequest sourceViewController];
-[LAPSPasscodeOptionsPresentationRequest initWithSourceViewController:];
```
