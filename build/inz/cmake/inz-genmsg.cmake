# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "inz: 2 messages, 0 services")

set(MSG_I_FLAGS "-Iinz:/home/leszek/armulti_simulator_ws/src/inz/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(inz_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/leszek/armulti_simulator_ws/src/inz/msg/Formation.msg" NAME_WE)
add_custom_target(_inz_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "inz" "/home/leszek/armulti_simulator_ws/src/inz/msg/Formation.msg" ""
)

get_filename_component(_filename "/home/leszek/armulti_simulator_ws/src/inz/msg/PoseTwist.msg" NAME_WE)
add_custom_target(_inz_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "inz" "/home/leszek/armulti_simulator_ws/src/inz/msg/PoseTwist.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(inz
  "/home/leszek/armulti_simulator_ws/src/inz/msg/Formation.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/inz
)
_generate_msg_cpp(inz
  "/home/leszek/armulti_simulator_ws/src/inz/msg/PoseTwist.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/inz
)

### Generating Services

### Generating Module File
_generate_module_cpp(inz
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/inz
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(inz_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(inz_generate_messages inz_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/leszek/armulti_simulator_ws/src/inz/msg/Formation.msg" NAME_WE)
add_dependencies(inz_generate_messages_cpp _inz_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/leszek/armulti_simulator_ws/src/inz/msg/PoseTwist.msg" NAME_WE)
add_dependencies(inz_generate_messages_cpp _inz_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(inz_gencpp)
add_dependencies(inz_gencpp inz_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS inz_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(inz
  "/home/leszek/armulti_simulator_ws/src/inz/msg/Formation.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/inz
)
_generate_msg_lisp(inz
  "/home/leszek/armulti_simulator_ws/src/inz/msg/PoseTwist.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/inz
)

### Generating Services

### Generating Module File
_generate_module_lisp(inz
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/inz
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(inz_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(inz_generate_messages inz_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/leszek/armulti_simulator_ws/src/inz/msg/Formation.msg" NAME_WE)
add_dependencies(inz_generate_messages_lisp _inz_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/leszek/armulti_simulator_ws/src/inz/msg/PoseTwist.msg" NAME_WE)
add_dependencies(inz_generate_messages_lisp _inz_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(inz_genlisp)
add_dependencies(inz_genlisp inz_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS inz_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(inz
  "/home/leszek/armulti_simulator_ws/src/inz/msg/Formation.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/inz
)
_generate_msg_py(inz
  "/home/leszek/armulti_simulator_ws/src/inz/msg/PoseTwist.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/inz
)

### Generating Services

### Generating Module File
_generate_module_py(inz
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/inz
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(inz_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(inz_generate_messages inz_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/leszek/armulti_simulator_ws/src/inz/msg/Formation.msg" NAME_WE)
add_dependencies(inz_generate_messages_py _inz_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/leszek/armulti_simulator_ws/src/inz/msg/PoseTwist.msg" NAME_WE)
add_dependencies(inz_generate_messages_py _inz_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(inz_genpy)
add_dependencies(inz_genpy inz_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS inz_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/inz)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/inz
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(inz_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/inz)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/inz
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(inz_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/inz)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/inz\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/inz
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(inz_generate_messages_py std_msgs_generate_messages_py)
endif()
