# `NSURLSessionTaskDependency`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 3 class methods

## Instance variables

```
@"NSURLSessionTaskDependencyDescription" _taskDependencyDescription;
@"NSURLSessionTask" _parentTask;
@"NSURLSessionTask" _mainDocumentTask;
```

## Properties

```
@property (T@"NSURLSessionTaskDependencyDescription",&,N,V_taskDependencyDescription) taskDependencyDescription;
@property (T@"NSURLSessionTask",R,&,N,V_parentTask) parentTask;
@property (T@"NSURLSessionTask",R,&,N,V_mainDocumentTask) mainDocumentTask;
```

## Class methods

```
+[NSURLSessionTaskDependency taskDependencyWithMainDocumentTask:];
+[NSURLSessionTaskDependency taskDependencyWithMainDocumentTask:taskDependencyDescription:];
+[NSURLSessionTaskDependency taskDependencyWithParentTask:priority:exclusive:];
```

## Instance methods

```
-[NSURLSessionTaskDependency dealloc];
-[NSURLSessionTaskDependency mainDocumentTask];
-[NSURLSessionTaskDependency parentTask];
-[NSURLSessionTaskDependency setTaskDependencyDescription:];
-[NSURLSessionTaskDependency taskDependencyDescription];
```
