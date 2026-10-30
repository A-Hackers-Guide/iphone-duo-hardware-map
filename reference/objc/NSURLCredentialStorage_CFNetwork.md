# `NSURLCredentialStorage`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSURLCredentialStorageInternal" _internal;
```

## Properties

```
@property (TB,N) _useSystemKeychain;
@property (T@"NSDictionary",R,C) allCredentials;
```

## Class methods

```
+[NSURLCredentialStorage sharedCredentialStorage];
```

## Instance methods

```
-[NSURLCredentialStorage credentialsForProtectionSpace:];
-[NSURLCredentialStorage _useSystemKeychain];
-[NSURLCredentialStorage init];
-[NSURLCredentialStorage set_useSystemKeychain:];
-[NSURLCredentialStorage dealloc];
-[NSURLCredentialStorage defaultCredentialForProtectionSpace:];
-[NSURLCredentialStorage allCredentials];
-[NSURLCredentialStorage setCredential:forProtectionSpace:];
-[NSURLCredentialStorage setDefaultCredential:forProtectionSpace:task:];
-[NSURLCredentialStorage removeCredential:forProtectionSpace:options:task:];
-[NSURLCredentialStorage _initWithIdentifier:private:];
-[NSURLCredentialStorage getDefaultCredentialForProtectionSpace:task:completionHandler:];
-[NSURLCredentialStorage _allCredentialsWithAccessControlGroup:includeLegacyKeychain:];
-[NSURLCredentialStorage removeCredential:forProtectionSpace:];
-[NSURLCredentialStorage removeCredential:forProtectionSpace:options:];
-[NSURLCredentialStorage _CFURLCredentialStorage];
-[NSURLCredentialStorage setCredential:forProtectionSpace:task:];
-[NSURLCredentialStorage _initWithCFURLCredentialStorage:];
-[NSURLCredentialStorage setDefaultCredential:forProtectionSpace:];
-[NSURLCredentialStorage getCredentialsForProtectionSpace:task:completionHandler:];
```
