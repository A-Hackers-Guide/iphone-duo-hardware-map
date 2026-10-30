# `NSURLSessionTaskDependencyDescription`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 6 properties, 8 instance methods, 6 class methods

## Instance variables

```
B _exclusive;
f _priority;
```

## Properties

```
@property (Tf,N,V_priority) priority;
@property (TB,N,V_exclusive) exclusive;
@property (T@"NSString",R) dependentURLPath;
@property (T@"NSString",R) dependentMimeType;
@property (T@"NSString",R) parentURLPath;
@property (T@"NSString",R) parentMimeType;
```

## Class methods

```
+[NSURLSessionTaskDependencyDescription taskDependencyDescriptionWithMimeType:parentMimeType:];
+[NSURLSessionTaskDependencyDescription taskDependencyDescriptionWithMimeType:parentURLPath:];
+[NSURLSessionTaskDependencyDescription taskDependencyDescriptionWithParentMimeType:];
+[NSURLSessionTaskDependencyDescription taskDependencyDescriptionWithParentURLPath:];
+[NSURLSessionTaskDependencyDescription taskDependencyDescriptionWithURLPath:parentMimeType:];
+[NSURLSessionTaskDependencyDescription taskDependencyDescriptionWithURLPath:parentURLPath:];
```

## Instance methods

```
-[NSURLSessionTaskDependencyDescription priority];
-[NSURLSessionTaskDependencyDescription setPriority:];
-[NSURLSessionTaskDependencyDescription setExclusive:];
-[NSURLSessionTaskDependencyDescription exclusive];
-[NSURLSessionTaskDependencyDescription dependentMimeType];
-[NSURLSessionTaskDependencyDescription dependentURLPath];
-[NSURLSessionTaskDependencyDescription parentMimeType];
-[NSURLSessionTaskDependencyDescription parentURLPath];
```
