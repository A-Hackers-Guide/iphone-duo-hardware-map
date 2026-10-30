# `_UIClickPresentationAssisting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"_UIClickPresentation",&,N) presentation;
@property (T@?,C,N) lifecycleCompletion;
@property (T@?,C,N) keyboardAssertionInvalidationHandler;
```

## Instance methods

```
-[_UIClickPresentationAssisting presentation];
-[_UIClickPresentationAssisting setPresentation:];
-[_UIClickPresentationAssisting dismissWithReason:alongsideActions:completion:];
-[_UIClickPresentationAssisting setLifecycleCompletion:];
-[_UIClickPresentationAssisting presentFromSourcePreview:lifecycleCompletion:];
-[_UIClickPresentationAssisting initWithClickPresentation:];
-[_UIClickPresentationAssisting setKeyboardAssertionInvalidationHandler:];
-[_UIClickPresentationAssisting keyboardAssertionInvalidationHandler];
-[_UIClickPresentationAssisting lifecycleCompletion];
```
