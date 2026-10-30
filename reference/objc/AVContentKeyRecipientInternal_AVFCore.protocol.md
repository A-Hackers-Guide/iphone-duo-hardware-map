# `AVContentKeyRecipientInternal` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `AVContentKeyRecipient`, `NSObject`
- 0 instance variables, 2 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSUUID",?,R,N) uniqueIdentifier;
@property (TB,?,R,N) disallowsLoggingURLs;
```

## Instance methods

```
-[AVContentKeyRecipientInternal expire];
-[AVContentKeyRecipientInternal contentKeySession];
-[AVContentKeyRecipientInternal _attachToContentKeySession:contentKeyBoss:failedSinceAlreadyAttachedToAnotherSession:];
-[AVContentKeyRecipientInternal _attachedToExternalContentKeySession];
-[AVContentKeyRecipientInternal uniqueIdentifier];
-[AVContentKeyRecipientInternal disallowsLoggingURLs];
```
