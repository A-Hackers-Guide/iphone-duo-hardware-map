# `FigCaptureProprietaryDefaults`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSUserDefaults" _userDefaults;
@? _defaultsChangedHandler;
@"NSMutableSet" _observedKeys;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _changingDefaultsMyself;
```

## Class methods

```
+[FigCaptureProprietaryDefaults initialize];
```

## Instance methods

```
-[FigCaptureProprietaryDefaults observeValueForKeyPath:ofObject:change:context:];
-[FigCaptureProprietaryDefaults dealloc];
-[FigCaptureProprietaryDefaults objectForKey:];
-[FigCaptureProprietaryDefaults objectsForWildcardKey:];
-[FigCaptureProprietaryDefaults setObject:forKey:];
-[FigCaptureProprietaryDefaults setObject:forWildcardKey:];
-[FigCaptureProprietaryDefaults initWithDefaultsChangedHandler:];
-[FigCaptureProprietaryDefaults migrateDefaultsFromAppBundleID:toAppBundleID:];
-[FigCaptureProprietaryDefaults observeChangesForKey:];
-[FigCaptureProprietaryDefaults sendNotificationOfNewTransientValue:forKey:];
-[FigCaptureProprietaryDefaults stopObservingChangesForKey:];
```
