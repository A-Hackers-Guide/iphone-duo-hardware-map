# `LSLinkSecurityManager`

- Image: [`/System/Library/Frameworks/LinkSecurity.framework/LinkSecurity`](../userland/System__Library__Frameworks__LinkSecurity.framework__LinkSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
connection;
preferenceStore;
```

## Properties

```
@property (TB,N,R) hasFlaggedURLs;
```

## Class methods

```
+[LSLinkSecurityManager sharedManager];
```

## Instance methods

```
-[LSLinkSecurityManager init];
-[LSLinkSecurityManager addFlaggedURLs:];
-[LSLinkSecurityManager addFlaggedURL:];
-[LSLinkSecurityManager checkIsFlaggedURL:completion:];
-[LSLinkSecurityManager hasFlaggedURLs];
```
