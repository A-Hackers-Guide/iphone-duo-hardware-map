# `__NSCFURLSessionTaskGroup`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `__NSURLSessionTaskGroupForConfiguration`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSURLSessionConfiguration" _groupConfiguration_ivar;
@"NSURLSession" _groupSession_ivar;
```

## Properties

```
@property (T@"NSURLSessionConfiguration",R,W,D) _groupConfiguration;
@property (T@"NSURLSession",R,W,D) _groupSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[__NSCFURLSessionTaskGroup dataTaskWithRequest:completionHandler:];
-[__NSCFURLSessionTaskGroup dataTaskWithRequest:];
-[__NSCFURLSessionTaskGroup dealloc];
-[__NSCFURLSessionTaskGroup forwardingTargetForSelector:];
-[__NSCFURLSessionTaskGroup uploadTaskWithStreamedRequest:];
-[__NSCFURLSessionTaskGroup _groupConfiguration];
-[__NSCFURLSessionTaskGroup _groupSession];
```
