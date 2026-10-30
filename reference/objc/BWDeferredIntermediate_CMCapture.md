# `BWDeferredIntermediate`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 3 properties, 14 instance methods, 2 class methods

## Instance variables

```
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _lock;
{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]} _cv;
@"NSString" _tag;
@"NSURL" _URL;
q _settingsID;
B _prefetching;
B _dirty;
```

## Properties

```
@property (T@"NSString",R,N,V_tag) tag;
@property (T@"NSURL",R,N,V_URL) URL;
@property (Tq,N,V_settingsID) settingsID;
```

## Class methods

```
+[BWDeferredIntermediate supportsSecureCoding];
+[BWDeferredIntermediate initialize];
```

## Instance methods

```
-[BWDeferredIntermediate init];
-[BWDeferredIntermediate flush];
-[BWDeferredIntermediate dealloc];
-[BWDeferredIntermediate settingsID];
-[BWDeferredIntermediate encodeWithCoder:];
-[BWDeferredIntermediate setSettingsID:];
-[BWDeferredIntermediate tag];
-[BWDeferredIntermediate initWithCoder:];
-[BWDeferredIntermediate URL];
-[BWDeferredIntermediate fetchAndRetain:];
-[BWDeferredIntermediate _shortString];
-[BWDeferredIntermediate archive:];
-[BWDeferredIntermediate initWithTag:URL:];
-[BWDeferredIntermediate setURL:prefetchQueue:];
```
