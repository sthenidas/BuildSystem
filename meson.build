project('tutorial', 'cpp')

vulkandep = [dependency('vulkan-headers', version : '1.4.313.0'), dependency('moltenvk', version : '1.3.0'), dependency('vulkan', version:'1.4.313.0')]
glfwdep = dependency('glfw3', version : '3.4')
volkdep = dependency('volk', version : '1.4.313.0')
imguidep = dependency('imgui', version : '1.92.5')

executable('demo', ['src/main.cpp','src/imgui_impl_glfw.cpp','src/imgui_impl_vulkan.cpp'], dependencies : [vulkandep,glfwdep,volkdep,imguidep])
