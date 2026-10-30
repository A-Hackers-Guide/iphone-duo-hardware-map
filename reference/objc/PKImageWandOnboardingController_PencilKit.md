# `PKImageWandOnboardingController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKImageWandOnboardingViewControllerDelegate`, `UIKeyboardSceneDelegateVisibilityObserver`, `UIPencilInteractionDelegate`
- 5 instance variables, 4 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"UIViewController" _presentationViewController;
@"PKToolPicker" _toolPicker;
@"PKImageWandOnboarding" _imageWandOnboarding;
B _onboardingViewDidAppear;
@"<PKImageWandOnboardingControllerDelegate>" _delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKImageWandOnboardingController resetOnboarding];
+[PKImageWandOnboardingController canShowOnboardingView];
```

## Instance methods

```
-[PKImageWandOnboardingController pencilInteraction:didReceiveSqueeze:];
-[PKImageWandOnboardingController keyboardSceneDelegate:inputViewSetVisibilityDidChange:includedReset:];
-[PKImageWandOnboardingController _toolPickerWillShow:];
-[PKImageWandOnboardingController imageWandOnboardingControllerCanBecomeFirstResponder:];
-[PKImageWandOnboardingController imageWandOnboardingControllerDidSelectContinue:];
-[PKImageWandOnboardingController imageWandOnboardingControllerIsBeingDismissed:];
-[PKImageWandOnboardingController imageWandOnboardingControllerViewDidAppear:animated:];
-[PKImageWandOnboardingController showOnboardingView];
```
