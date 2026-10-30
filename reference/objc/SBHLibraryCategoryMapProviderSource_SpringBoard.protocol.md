# `SBHLibraryCategoryMapProviderSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"<SBHLibraryCategoryMapProviderSourceDelegate>",W,N) delegate;
@property (T@"NSString",R,N) sourceName;
```

## Instance methods

```
-[SBHLibraryCategoryMapProviderSource sourceName];
-[SBHLibraryCategoryMapProviderSource setDelegate:];
-[SBHLibraryCategoryMapProviderSource delegate];
-[SBHLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:];
```
