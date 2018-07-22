/*
 * The MIT License
 *
 * Copyright 2017-2018 Norwegian University of Technology
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
#include <fmuproxy/grpc/server/FmuServiceImpl.hpp>

using namespace std;
using namespace fmuproxy::grpc;
using namespace fmuproxy::grpc::server;

using google::protobuf::Empty;

FmuServiceImpl::FmuServiceImpl(fmuproxy::fmi::Fmu &fmu) : m_fmu(fmu) {}

::grpc::Status FmuServiceImpl::GetModelDescriptionXml(::grpc::ServerContext *context, const Empty *request, Str *response) {
    response->set_value(m_fmu.get_model_description_xml());
    return ::grpc::Status::OK;
}

//::grpc::Status FmuServiceImpl::GetModelDescription(::grpc::ServerContext *context, const Empty *request, ModelDescription *response) {
//    return Service::GetModelDescription(context, request, response);
//}
