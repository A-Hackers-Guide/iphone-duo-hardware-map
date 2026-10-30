# `PKGenerationModelAvailabilityController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIKeyboardSceneDelegateVisibilityObserver`
- 2 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
q _imageWandStatus;
q _generativePlaygroundStatus;
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
+[PKGenerationModelAvailabilityController sharedInstance];
```

## Instance methods

```
-[PKGenerationModelAvailabilityController prewarm];
-[PKGenerationModelAvailabilityController init];
-[PKGenerationModelAvailabilityController keyboardSceneDelegate:inputViewSetVisibilityDidChange:includedReset:];
-[PKGenerationModelAvailabilityController _handleModelAvailabilityStatusDidChange:forIdentifier:completion:];
-[PKGenerationModelAvailabilityController handleAvailabilityChange:];
-[PKGenerationModelAvailabilityController handleAvailabilityChange:forIdentifier:];
-[PKGenerationModelAvailabilityController isGenerationModelAvailabilityUndetermined];
-[PKGenerationModelAvailabilityController isGenerationModelAvailable];
-[PKGenerationModelAvailabilityController isGenerationModelAvailableForIdentifier:];
-[PKGenerationModelAvailabilityController isGenerationModelDisabled];
-[PKGenerationModelAvailabilityController nameAndAddressDescription];
-[PKGenerationModelAvailabilityController presentEnrollmentScreenViewControllerIfNecessaryInWindow:];
-[PKGenerationModelAvailabilityController presentGreymatterAvailabilityAlertControllerInWindow:];
-[PKGenerationModelAvailabilityController queryGenerationModelAvailabilityStatusWithCompletionHandler:];
-[PKGenerationModelAvailabilityController shouldShowEnrollmentUI];
-[PKGenerationModelAvailabilityController statusForIdentifier:];
-[PKGenerationModelAvailabilityController stringRepresentationOfAvailabilityStatus:];
```
