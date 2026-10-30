# `SymptomsBasebandClientDriver`

- Image: [`/System/Library/PrivateFrameworks/SymptomBasebandChannel.framework/SymptomBasebandChannel`](../userland/System__Library__PrivateFrameworks__SymptomBasebandChannel.framework__SymptomBasebandChannel.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
{shared_ptr<SymptomsARIClientWrapper>="__ptr_"^{SymptomsARIClientWrapper}"__cntrl_"^{__shared_weak_count}} _driver;
{queue="fObj"{object="fObj"@"NSObject<OS_dispatch_object>"}} _queue;
B _clientActive;
```

## Class methods

```
+[SymptomsBasebandClientDriver sharedInstance];
```

## Instance methods

```
-[SymptomsBasebandClientDriver init];
-[SymptomsBasebandClientDriver setCellularIdleStatus:forSubscription:confidence:completion:];
-[SymptomsBasebandClientDriver _ariClientStarted];
-[SymptomsBasebandClientDriver _ariClientStopped];
-[SymptomsBasebandClientDriver _handleCellularIdleStatusResponse:size:completion:];
-[SymptomsBasebandClientDriver _handleRegistrationInfoResponse:size:completion:];
-[SymptomsBasebandClientDriver _handleSignalStrengthResponse:size:completion:];
-[SymptomsBasebandClientDriver requestRegistrationInfoForSubscription:completion:];
-[SymptomsBasebandClientDriver requestSignalStrengthForSubscription:completion:];
```
