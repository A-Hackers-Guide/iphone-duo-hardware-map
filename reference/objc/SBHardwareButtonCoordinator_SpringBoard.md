# `SBHardwareButtonCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
i _sysdiagnoseDidBeginNotificationToken;
@"SBWindowScene" _windowScene;
@"NSDictionary" _buttonIdentifierToButtonInstance;
@"NSCountedSet" _canceledButtonIdentifiers;
@"NSCountedSet" _activeButtonIdentifiers;
@"NSDictionary" _buttonIdentifierToSuppressedButtonIdentifiers;
@"NSSet" _otherButtonsAlwaysSuppressButtonIdentifiers;
@"NSDictionary" _suppressedButtonIdentifierToSuppressorButtonIdentifiers;
```

## Instance methods

```
-[SBHardwareButtonCoordinator dealloc];
-[SBHardwareButtonCoordinator assertButtonIsActive:];
-[SBHardwareButtonCoordinator assertButtonIsActive:dropletHintIdentifier:];
-[SBHardwareButtonCoordinator buttonShouldStart:];
-[SBHardwareButtonCoordinator cancelHardwareButtons:fromButton:];
```
