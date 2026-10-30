# `MLUpdatable` (protocol)

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MLModeling`, `MLWritable`
- 0 instance variables, 0 properties, 5 instance methods, 1 class methods

## Class methods

```
+[MLUpdatable loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLUpdatable updateModelWithData:];
-[MLUpdatable cancelUpdate];
-[MLUpdatable resumeUpdateWithParameters:];
-[MLUpdatable setUpdateProgressHandlers:dispatchQueue:];
-[MLUpdatable resumeUpdate];
```
