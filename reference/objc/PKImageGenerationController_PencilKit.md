# `PKImageGenerationController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _cachedShouldShowImageGenerationUI;
@"<PKImageGenerationControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<PKImageGenerationControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) isGenerationToolEnabled;
@property (TB,R,N) isImageGenerationAllowed;
@property (TB,R,N) isGenerationModelAvailable;
@property (TB,R,N) shouldShowImageGenerationUI;
@property (TB,R,N) shouldAddMagicWand;
```

## Instance methods

```
-[PKImageGenerationController init];
-[PKImageGenerationController setDelegate:];
-[PKImageGenerationController delegate];
-[PKImageGenerationController isImageGenerationAllowed];
-[PKImageGenerationController shouldShowImageGenerationUI];
-[PKImageGenerationController _handleGenerationModelAvailabilityDidChangeNotification:];
-[PKImageGenerationController _handleManagedConfigurationEffectiveSettingsDidChangeNotification:];
-[PKImageGenerationController _notifyStateDidChangeIfNecessary];
-[PKImageGenerationController isGenerationModelAvailable];
-[PKImageGenerationController isGenerationToolEnabled];
-[PKImageGenerationController shouldAddMagicWand];
```
