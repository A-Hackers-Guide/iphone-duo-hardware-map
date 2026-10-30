# `UIWebGeolocationPolicyDecider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 23 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _sites;
@"NSMutableArray" _challenges;
@"NSMapTable" _activeChallenges;
```

## Class methods

```
+[UIWebGeolocationPolicyDecider initialize];
+[UIWebGeolocationPolicyDecider sharedPolicyDecider];
```

## Instance methods

```
-[UIWebGeolocationPolicyDecider clearCache];
-[UIWebGeolocationPolicyDecider init];
-[UIWebGeolocationPolicyDecider _save];
-[UIWebGeolocationPolicyDecider dealloc];
-[UIWebGeolocationPolicyDecider clearAllCaches];
-[UIWebGeolocationPolicyDecider _load];
-[UIWebGeolocationPolicyDecider _addChallengeCount:forToken:requestingURL:];
-[UIWebGeolocationPolicyDecider _decidePolicyForGeolocationRequestFromOrigin:requestingURL:view:listener:];
-[UIWebGeolocationPolicyDecider _executeNextChallenge];
-[UIWebGeolocationPolicyDecider _getAuthorizationStatusForToken:userVisibleDomain:requestingURL:promptInfo:];
-[UIWebGeolocationPolicyDecider _getChallengeCountFromHistoryForToken:requestingURL:];
-[UIWebGeolocationPolicyDecider _isAuthorizationDate:inclusivelyBetweenDate:andDate:];
-[UIWebGeolocationPolicyDecider _siteFile];
-[UIWebGeolocationPolicyDecider _siteFileInContainerDirectory:creatingIntermediateDirectoriesIfNecessary:];
-[UIWebGeolocationPolicyDecider clearAuthorizationForDomain:];
-[UIWebGeolocationPolicyDecider clearAuthorizationsAddedBetween:and:];
-[UIWebGeolocationPolicyDecider clearSafariCache];
-[UIWebGeolocationPolicyDecider decidePolicyForGeolocationRequestFromOrigin:requestingURL:view:listener:];
-[UIWebGeolocationPolicyDecider decidePolicyForGeolocationRequestFromOrigin:requestingURL:window:listener:];
-[UIWebGeolocationPolicyDecider didAuthorizeGeolocationForPromptInfo:];
-[UIWebGeolocationPolicyDecider didDenyGeolocationForPromptInfo:];
-[UIWebGeolocationPolicyDecider getAuthorizationStatusForOrigin:requestingURL:promptInfo:];
-[UIWebGeolocationPolicyDecider webView:decidePolicyForGeolocationRequestFromOrigin:frame:listener:];
```
