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

#include <ctime>
#include <vector>
#include <iostream>

#include "TestUtil.cpp"
#include "fmuproxy/fmi/Fmu.hpp"

using namespace std;
using namespace fmuproxy::fmi;

const double start = 0;
const double stop = 10;
const double step_size = 1E-4;

int main(int argc, char **argv) {

    string fmu_path = string(getenv("TEST_FMUs"))
                      + "/FMI_2.0/CoSimulation/" + getOs() +
                      "/20sim/4.6.4.8004/ControlledTemperature/ControlledTemperature.fmu";

    Fmu fmu = Fmu(fmu_path.c_str());

    const auto instance = fmu.new_instance();

    instance->init();

    clock_t begin = clock();

    vector<fmi2_value_reference_t> vr = {instance->get_value_reference("Temperature_Reference"), instance->get_value_reference("Temperature_Room")};
    vector<fmi2_real_t> ref(2);

    while (instance->getCurrentTime() <= stop-step_size) {
        fmi2_status_t status = instance->step(step_size);
        if (status != fmi2_status_ok) {
            cout << "Error! step returned with status: " << fmi2_status_to_string(status) << endl;
            break;
        }
        instance->readReal(vr, ref);
//        cout << "Temperature_Reference=" << ref[0] << ", Temperature_Room=" << ref[1] << endl;
    }

    clock_t end = clock();

    double elapsed_secs = double(end-begin) / CLOCKS_PER_SEC;
    cout << "elapsed=" << elapsed_secs << "s" << endl;

    instance->terminate();

    return 0;

}