# `SFAuthenticationManagerDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance methods

```
-[SFAuthenticationManagerDelegate manager:didCompleteAuthenticationForSessionWithID:];
-[SFAuthenticationManagerDelegate manager:didDisableAuthenticationForSessionWithID:];
-[SFAuthenticationManagerDelegate manager:didEnableAuthenticationForSessionWithID:];
-[SFAuthenticationManagerDelegate manager:didFailApproveForSessionWithID:error:];
-[SFAuthenticationManagerDelegate manager:didFailAuthenticationForSessionWithID:error:];
-[SFAuthenticationManagerDelegate manager:didFailToDisableDeviceForSessionWithID:error:];
-[SFAuthenticationManagerDelegate manager:didFailToEnableDeviceForSessionWithID:error:];
-[SFAuthenticationManagerDelegate manager:didReceiveRequestToApproveForSessionID:info:completionHandler:];
-[SFAuthenticationManagerDelegate manager:didReceiveRequestToApproveForSessionWithID:info:completionHandler:];
-[SFAuthenticationManagerDelegate manager:didStartAuthenticationForSessionWithID:];
```
