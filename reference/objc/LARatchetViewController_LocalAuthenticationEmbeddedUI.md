# `LARatchetViewController`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 9 instance variables, 4 properties, 22 instance methods, 2 class methods

## Instance variables

```
B _isInViewHierarchy;
@"<LACUIRatchetViewModelType>" _viewModel;
@"UIPageViewController" _pageViewController;
@"NSArray" _subscriptions;
@"NSDictionary" _internalOptions;
@"UIViewController" _presentationContext;
@"NSDictionary" _options;
@"LARatchetViewControllerConfiguration" _configuration;
@"<LARatchetViewControllerDelegate>" _delegate;
```

## Properties

```
@property (TB,R,N) isInViewHierarchy;
@property (T@"NSDictionary",R,N,V_options) options;
@property (T@"LARatchetViewControllerConfiguration",R,N,V_configuration) configuration;
@property (T@"<LARatchetViewControllerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[LARatchetViewController makeViewControllerWithOptions:];
+[LARatchetViewController makeViewControllerWithOptions:configuration:];
```

## Instance methods

```
-[LARatchetViewController finishWithResult:error:];
-[LARatchetViewController subscriptions];
-[LARatchetViewController viewModel];
-[LARatchetViewController presentationContext];
-[LARatchetViewController setViewModel:];
-[LARatchetViewController dealloc];
-[LARatchetViewController invalidate];
-[LARatchetViewController setDelegate:];
-[LARatchetViewController viewDidAppear:];
-[LARatchetViewController configuration];
-[LARatchetViewController delegate];
-[LARatchetViewController pageViewController];
-[LARatchetViewController viewDidDisappear:];
-[LARatchetViewController setSubscriptions:];
-[LARatchetViewController options];
-[LARatchetViewController clean];
-[LARatchetViewController evaluateAndPresentViewController];
-[LARatchetViewController evaluateAndShowViewController];
-[LARatchetViewController internalOptions];
-[LARatchetViewController initWithOptions:configuration:];
-[LARatchetViewController isInViewHierarchy];
-[LARatchetViewController setIsInViewHierarchy:];
```
